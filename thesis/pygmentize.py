#!/usr/bin/env python3

"""
    pygments.lexers.html
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for HTML, XML and related markup.

    :copyright: Copyright 2006-2023 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

import argparse
import sys
import pygments.cmdline as _cmdline
from pygments.lexer import DelegatingLexer, RegexLexer, ExtendedRegexLexer, include, bygroups, \
    default, using
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Punctuation, Whitespace, Number, Other
from pygments.util import looks_like_xml, html_doctype_matches
import pygments.unistring as uni

from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.jvm import ScalaLexer
from pygments.lexers.css import CssLexer, _indentation, _starts_block
from pygments.lexers.ruby import RubyLexer

__all__ = ['SvelteLexer']

JS_IDENT_START = ('(?:[$_' + uni.combine('Lu', 'Ll', 'Lt', 'Lm', 'Lo', 'Nl') +
                  ']|\\\\u[a-fA-F0-9]{4})')
JS_IDENT_PART = ('(?:[$' + uni.combine('Lu', 'Ll', 'Lt', 'Lm', 'Lo', 'Nl',
                                       'Mn', 'Mc', 'Nd', 'Pc') +
                 '\u200c\u200d]|\\\\u[a-fA-F0-9]{4})')
JS_IDENT = JS_IDENT_START + '(?:' + JS_IDENT_PART + ')*'


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', dest='lexer', type=str)
    opts, rest = parser.parse_known_args(args[1:])
    if opts.lexer == 'svelte':
        args = [__file__, '-l', __file__ + ':SvelteLexer', '-x', *rest]
    _cmdline.main(args)


class SvelteLexer(RegexLexer):
    """
    For Svelte source code.
    """

    name = 'Svelte'
    aliases = ['svelte']
    filenames = ['*.svelte']
    mimetypes = ['application/svelte']

    flags = re.DOTALL | re.MULTILINE

    tokens = {
        'root': [
            ('[^{<&]+', Text),
            ('{', Punctuation, 'svelte-base'),
            (r'&\S*?;', Name.Entity),
            (r'\<\!\[CDATA\[.*?\]\]\>', Comment.Preproc),
            (r'<!--.*?-->', Comment.Multiline),
            (r'<\?.*?\?>', Comment.Preproc),
            ('<![^>]*>', Comment.Preproc),
            (r'(<)(\s*)(script)(\s*)',
             bygroups(Punctuation, Text, Name.Tag, Text),
             ('script-content', 'tag')),
            (r'(<)(\s*)(style)(\s*)',
             bygroups(Punctuation, Text, Name.Tag, Text),
             ('style-content', 'tag')),
            # note: this allows tag names not used in HTML like <x:with-dash>,
            # this is to support yet-unknown template engines and the like
            (r'(<)(\s*)([\w:.-]+)',
             bygroups(Punctuation, Text, Name.Tag), 'tag'),
            (r'(<)(\s*)(/)(\s*)([\w:.-]+)(\s*)(>)',
             bygroups(Punctuation, Text, Punctuation, Text, Name.Tag, Text,
                      Punctuation)),
        ],
        'tag': [
            (r'\s+', Text),
            (r'{', Punctuation,
             'js-base'),
            (r'([\w-]+:)([\w-]+)(=)(\s*)', bygroups(Operator, Name.Attribute, Operator, Text),
             'attr'),
            (r'([\w-]+\s*)(=)(\s*)', bygroups(Name.Attribute, Operator, Text),
             'attr'),
            (r'([\w-]+:)([\w-])', bygroups(Operator, Name.Attribute)),
            (r'[\w-]+', Name.Attribute),
            (r'(/?)(\s*)(>)', bygroups(Punctuation, Text, Punctuation), '#pop'),
        ],
        'script-content': [
            (r'(<)(\s*)(/)(\s*)(script)(\s*)(>)',
             bygroups(Punctuation, Text, Punctuation, Text, Name.Tag, Text,
                      Punctuation), '#pop'),
            (r'.+?(?=<\s*/\s*script\s*>)', using(JavascriptLexer)),
            # fallback cases for when there is no closing script tag
            # first look for newline and then go back into root state
            # if that fails just read the rest of the file
            # this is similar to the error handling logic in lexer.py
            (r'.+?\n', using(JavascriptLexer), '#pop'),
            (r'.+', using(JavascriptLexer), '#pop'),
        ],
        'style-content': [
            (r'(<)(\s*)(/)(\s*)(style)(\s*)(>)',
             bygroups(Punctuation, Text, Punctuation, Text, Name.Tag, Text,
                      Punctuation),'#pop'),
            (r'.+?(?=<\s*/\s*style\s*>)', using(CssLexer)),
            # fallback cases for when there is no closing style tag
            # first look for newline and then go back into root state
            # if that fails just read the rest of the file
            # this is similar to the error handling logic in lexer.py
            (r'.+?\n', using(CssLexer), '#pop'),
            (r'.+', using(CssLexer), '#pop'),
        ],
        'attr': [
            ('{', Punctuation, ('#pop','js-base')),
            ('".*?"', String, '#pop'),
            ("'.*?'", String, '#pop'),
            (r'[^\s>]+', String, '#pop'),
        ],
        'commentsandwhitespace': [
            (r'\s+', Whitespace),
            (r'<!--', Comment),
            (r'//.*?$', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline)
        ],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            (r'/(\\.|[^[/\\\n]|\[(\\.|[^\]\\\n])*])+/'
             r'([gimuysd]+\b|\B)', String.Regex, '#pop'),
            (r'(?=/)', Text, ('#pop', 'badregex')),
            default('#pop')
        ],
        'badregex': [
            (r'\n', Whitespace, '#pop')
        ],
        'svelte-base': [
            (r'(\#)(if)', bygroups(Punctuation, Name.Tag), ('#pop', 'js-base')),
            (r'(\#)(each)', bygroups(Punctuation, Name.Tag), ('#pop', 'js-base')),
            (r'([\:\/])(\w*)(})', bygroups(Punctuation, Name.Tag, Punctuation), '#pop'),
            ('', Text, ('#pop', 'js-base'))
        ],
        'js-base': [
            ('}', Punctuation, '#pop'),
            (r'\A#! ?/.*?$', Comment.Hashbang),  # recognized by node.js
            (r'^(?=\s|/|<!--)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),

            # Numeric literals
            (r'0[bB][01]+n?', Number.Bin),
            (r'0[oO]?[0-7]+n?', Number.Oct),  # Browsers support "0o7" and "07" (< ES5) notations
            (r'0[xX][0-9a-fA-F]+n?', Number.Hex),
            (r'[0-9]+n', Number.Integer),  # Javascript BigInt requires an "n" postfix
            # Javascript doesn't have actual integer literals, so every other
            # numeric literal is handled by the regex below (including "normal")
            # integers
            (r'(\.[0-9]+|[0-9]+\.[0-9]*|[0-9]+)([eE][-+]?[0-9]+)?', Number.Float),

            (r'\.\.\.|=>', Punctuation),
            (r'\+\+|--|~|\?\?=?|\?|:|\\(?=\n)|'
             r'(<<|>>>?|==?|!=?|(?:\*\*|\|\||&&|[-<>+*%&|^/]))=?', Operator, 'slashstartsregex'),
            (r'[{(\[;,]', Punctuation, 'slashstartsregex'),
            (r'[})\].]', Punctuation),

            (r'(typeof|instanceof|in|void|delete|new)\b', Operator.Word, 'slashstartsregex'),

            # Match stuff like: constructor
            (r'\b(constructor|from|as)\b', Keyword.Reserved),

            (r'(for|in|while|do|break|return|continue|switch|case|default|if|else|'
             r'throw|try|catch|finally|yield|await|async|this|of|static|export|'
             r'import|debugger|extends|super)\b', Keyword, 'slashstartsregex'),
            (r'(var|let|const|with|function|class)\b', Keyword.Declaration, 'slashstartsregex'),

            (r'(abstract|boolean|byte|char|double|enum|final|float|goto|'
             r'implements|int|interface|long|native|package|private|protected|'
             r'public|short|synchronized|throws|transient|volatile)\b', Keyword.Reserved),
            (r'(true|false|null|NaN|Infinity|undefined)\b', Keyword.Constant),

            (r'(Array|Boolean|Date|BigInt|Function|Math|ArrayBuffer|'
             r'Number|Object|RegExp|String|Promise|Proxy|decodeURI|'
             r'decodeURIComponent|encodeURI|encodeURIComponent|'
             r'eval|isFinite|isNaN|parseFloat|parseInt|DataView|'
             r'document|window|globalThis|global|Symbol|Intl|'
             r'WeakSet|WeakMap|Set|Map|Reflect|JSON|Atomics|'
             r'Int(?:8|16|32)Array|BigInt64Array|Float32Array|Float64Array|'
             r'Uint8ClampedArray|Uint(?:8|16|32)Array|BigUint64Array)\b', Name.Builtin),

            (r'((?:Eval|Internal|Range|Reference|Syntax|Type|URI)?Error)\b', Name.Exception),

            # Match stuff like: super(argument, list)
            (r'(super)(\s*)(\([\w,?.$\s]+\s*\))',
             bygroups(Keyword, Whitespace), 'slashstartsregex'),
            # Match stuff like: function() {...}
            (r'([a-zA-Z_?.$][\w?.$]*)(?=\(\) \{)', Name.Other, 'slashstartsregex'),

            (JS_IDENT, Name.Other),
            (r'"(\\\\|\\[^\\]|[^"\\])*"', String.Double),
            (r"'(\\\\|\\[^\\]|[^'\\])*'", String.Single),
            (r'`', String.Backtick, 'interp'),
        ],
        'interp': [
            (r'`', String.Backtick, '#pop'),
            (r'\\.', String.Backtick),
            (r'\$\{', String.Interpol, 'interp-inside'),
            (r'\$', String.Backtick),
            (r'[^`\\$]+', String.Backtick),
        ],
        'interp-inside': [
            # TODO: should this include single-line comments and allow nesting strings?
            (r'\}', String.Interpol, '#pop'),
            include('root'),
        ],
    }

if __name__ == '__main__':
    main(sys.argv)
