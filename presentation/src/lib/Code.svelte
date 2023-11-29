<script>
  /** 
   * @type {{ 
   * id?: string,
   * class?: string,
   * children?: any,
   * trim?: boolean,
   * noescape?: boolean,
   * lineNumbers?: string | boolean,
   * lineStartFrom?: string
   * }} */
  let {
    id = undefined,
    class: clazz = "",
    children,
    trim = false,
    noescape = false,
    lineNumbers = undefined,
    lineStartFrom = undefined,
  } = $props();
</script>

<pre data-id={id}>
	<code
    class={"!overflow-hidden " + clazz}
    data-trim={trim || undefined}
    data-noescape={noescape || undefined}
    data-line-numbers={lineNumbers}
    data-ln-start-from={lineStartFrom}>
{@render children()}
  </code>
</pre>
