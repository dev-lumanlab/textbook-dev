<script>
	import SearchContents from '$lib/components/SearchContents.svelte';
	import { searchPublishedArticles } from '$lib/api/docs';
	import { onDestroy, onMount } from 'svelte';

	let contents = [];
	let search = '';
	let resultStatsText = '';
	let markSearch = '';

	let observeTarget;
	let intersectionObserver;
	let loadingMore = false;
	let total = 0;
	let currentPage = 1;
	let limit = 10;

	$: maxRequestCount = Math.ceil(total / limit);

	const onSubmit = async () => {
		try {
			intersectionObserver?.unobserve(observeTarget);
			contents = [];
			currentPage = 1;
			const { newItems, contentsLength } = await getContents();
			total = contentsLength;
			markSearch = search;
			contents = [...newItems];
			currentPage += 1;
			if (total > 0) {
				resultStatsText = `You found ${total} results for "${search}"`;
			} else {
				resultStatsText = `No results found for "${search}"`;
			}
			intersectionObserver?.observe(observeTarget);
		} catch (error) {
			console.error(error);
		}
	};

	const getContents = async () => {
		try {
			const response = await searchPublishedArticles(search, currentPage, limit);
			const newItems = response.data.content.articles;
			const contentsLength = response.data.content.total;

			return { newItems, contentsLength };
		} catch (error) {
			console.error(error);
		}
	};

	const loadMore = async (entries) => {
		if (loadingMore || entries[0].isIntersecting === false || maxRequestCount < currentPage) return;
		loadingMore = true;
		const { newItems } = await getContents();
		contents = [...contents, ...newItems];
		currentPage += 1;
		loadingMore = false;
	};

	onMount(() => {
		intersectionObserver = new IntersectionObserver(loadMore, {
			rootMargin: '100px' // 뷰포트 끝에서 100px 전에 로드
		});
	});

	onDestroy(() => {
		intersectionObserver?.disconnect();
	});
</script>

<svelte:head>
	<title>Search - IACAPAP</title>
</svelte:head>

<div class="search-wrap">
	<form on:submit|preventDefault={onSubmit}>
		<div class="input-wrap">
			<input type="text" placeholder="Search...." bind:value={search} />
			<button type="submit" class="search-btn"></button>
		</div>
	</form>
</div>

<h2>{resultStatsText}</h2>

<SearchContents {markSearch} {contents} bind:observeTarget />

<style lang="scss">
	.search-wrap {
		margin-top: 8px;
		margin-bottom: 40px;
		.input-wrap {
			position: relative;

			input {
				width: 100%;
				height: 84px;
				padding: 24px 82px 24px 40px;
				border: 1px solid #e1e4e8;
				border-radius: 99px;
				font-size: 26px;
				line-height: 36px;

				&::placeholder {
					color: var(--slate-base-color);
				}
			}
			.search-btn {
				position: absolute;
				background-color: var(--blue-color);
				border-radius: 100%;
				top: 0;
				bottom: 0;
				margin: auto;
				right: 14px;
				width: 56px;
				height: 56px;
				background-image: url('/search.png');
				background-size: auto;
				background-position: center;
				background-repeat: no-repeat;
			}
		}
	}

	h2 {
		font-size: 40px;
		line-height: 50px;
		font-weight: 500;
		margin: 40px 0;
	}
</style>
