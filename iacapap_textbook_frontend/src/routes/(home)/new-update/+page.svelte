<script>
	import { getPublishingArticleList } from '$lib/api/docs';
	import InfiniteScroll from '$lib/components/InfiniteScroll.svelte';
	import { DocsList, EmptyContent } from '$lib/components/docs';

	let contents = [];
	let currentPage = 1;
	let limit = 10;
	let observeTarget;

	const getContents = async () => {
		try {
			const response = await getPublishingArticleList(currentPage, limit);
			const newItems = response.data.content.articles;
			const contentsLength = response.data.content.total;

			return { newItems, contentsLength };
		} catch (error) {
			console.error(error);
		}
	};
</script>

<svelte:head>
	<title>New Update - IACAPAP</title>
</svelte:head>

<InfiniteScroll {getContents} {observeTarget} {limit} bind:contents bind:currentPage>
	<h2>List of recently updated textbooks</h2>
	<div class="contents">
		{#if contents.length > 0}
			<DocsList {contents} alignItemsCenter={true} bind:observeTarget />
		{:else}
			<EmptyContent description="There is no recently updated list of subjects." />
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
