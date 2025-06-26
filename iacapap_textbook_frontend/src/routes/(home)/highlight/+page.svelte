<script>
	import { getHighlightList } from '$lib/api/docs';
	import InfiniteScroll from '$lib/components/InfiniteScroll.svelte';
	import { DocsList, EmptyContent } from '$lib/components/docs';

	let contents = [];
	let currentPage = 1;
	let limit = 10;
	let observeTarget;

	const getContents = async () => {
		try {
			const response = await getHighlightList(currentPage, limit);
			const highlights = response.data.content.highlights;
			const newItems = highlights.map((highlight) => {
				return {
					id: highlight.article_id,
					title: highlight.text,
					book: highlight.book,
					chapter: highlight.chapter,
					last_update: highlight.created_at
				};
			});
			const contentsLength = response.data.content.total;

			return { newItems, contentsLength };
		} catch (error) {
			console.error(error);
		}
	};
</script>

<svelte:head>
	<title>Highlight - IACAPAP</title>
</svelte:head>
<InfiniteScroll {getContents} {observeTarget} {limit} bind:contents bind:currentPage>
	<h2>Highlight</h2>
	<div class="contents">
		{#if contents.length > 0}
			<DocsList {contents} includeSeconds={true} bind:observeTarget />
		{:else}
			<EmptyContent description="There are no highlights." />
		{/if}
	</div>
</InfiniteScroll>

<style lang="scss">
	h2 {
		font-size: 24px;
		line-height: 30px;
		margin-bottom: 16px;
	}

	.contents {
		padding-bottom: 75px;
	}
</style>
