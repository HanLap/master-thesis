<script>
  export let id = undefined;
  let clazz = "";
  export { clazz as class };
  export let trim = false;
  export let noescape = false;
  export let lineNumbers = undefined;
  export let lineStartFrom = undefined;
</script>

<pre data-id={id}>
		<code
    class={'!overflow-hidden ' + clazz}
    data-trim={trim || undefined}
    data-noescape={noescape || undefined}
    data-line-numbers={lineNumbers}
    data-ln-start-from={lineStartFrom}>
				<slot />
		</code>
</pre>
