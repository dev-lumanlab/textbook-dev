<script>
	import { onMount } from 'svelte';
	import tocbot from 'tocbot';
	import '$styles/toc.scss';

	onMount(() => {
		tocbot.init({
			tocSelector: '#toc',
			contentSelector: '.content',
			headingSelector: 'h2, h3, h4',
			scrollSmooth: true,
			collapseDepth: 0,
			hasInnerContainers: true
		});
	});
</script>

<div id="toc"></div>
