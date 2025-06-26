<script>
	import { onDestroy, onMount } from 'svelte';

	export let observeTarget;
	export let currentPage;
	export let limit;
	/**
	 * 비동기로 콘텐츠를 가져오는 함수입니다.
	 * @async
	 * @function getContents
	 * @returns {Promise<{ newItems: Array<Object>, contentsLength: number }>} 비동기 작업의 결과를 담은 객체를 반환합니다.
	 */
	export let getContents;
	export let contents;

	let intersectionObserver;
	let loadingMore = false;
	let total = 0;

	$: maxRequestCount = Math.ceil(total / limit);

	const loadInitialItems = async () => {
		const { newItems, contentsLength } = await getContents();
		contents = [...newItems];
		total = contentsLength;
		currentPage += 1;
	};

	const loadMore = async () => {
		const { newItems } = await getContents();
		contents = [...contents, ...newItems];
		currentPage += 1;
	};

	onMount(() => {
		intersectionObserver = new IntersectionObserver(
			(entries) => {
				if (loadingMore || entries[0].isIntersecting === false || maxRequestCount < currentPage)
					return;
				loadingMore = true;
				loadMore(entries);
				loadingMore = false;
			},
			{
				rootMargin: '100px' // 뷰포트 끝에서 100px 전에 로드
			}
		);

		loadInitialItems();
	});

	onDestroy(() => {
		if (intersectionObserver) {
			intersectionObserver.disconnect();
		}
	});

	$: if (observeTarget) {
		intersectionObserver.observe(observeTarget);
	}
</script>

<slot />
