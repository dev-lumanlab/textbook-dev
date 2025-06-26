<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { highlightStore } from '../../../stores/highlight';
	import { goto } from '$app/navigation';
	import { docTabStore } from '$stores/docTab';
	import Topic from '$lib/components/docs/Topic.svelte';
	import Graphics from '$lib/components/docs/Graphics.svelte';

	export let data;

	$: articleId = $page.params.id;

	$: if (data.content === null) {
		alert('해당 문서가 존재하지 않습니다.');
		goto('/');
	}

	onMount(() => {
		docTabStore.change('topic');
		highlightStore.get(articleId);
	});
</script>

<svelte:head>
	<title>{data.content.book} - IACAPAP</title>
</svelte:head>

<div id="capture" class="container">
	{#if data.content}
		{#if $docTabStore === 'topic'}
			<Topic {data} {articleId} />
		{:else}
			<Graphics {data} />
		{/if}
	{/if}
</div>

<style lang="scss">
	.container {
		padding: 24px;
	}
</style>
