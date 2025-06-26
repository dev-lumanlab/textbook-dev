<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { SwiperNext, SwiperPrev } from '$lib/components/icons';

	export let totalPages;

	$: currentPage = Number($page.url.searchParams.get('page')) || 1;
	$: startPage = Math.max(currentPage - 2, 1);
	$: endPage = Math.min(currentPage + 2, totalPages);

	const gotoPage = (page) => {
		goto(`?page=${page}`);
	};

	const handleNext = () => {
		const nextPage = currentPage + 10;
		if (nextPage > totalPages) {
			gotoPage(totalPages);
		} else {
			gotoPage(nextPage);
		}
	};

	const handlePrev = () => {
		const prevPage = currentPage - 10;
		if (prevPage < 1) {
			gotoPage(1);
		} else {
			gotoPage(prevPage);
		}
	};
</script>

<div class="pagination">
	{#if currentPage !== 1}
		<button on:click={handlePrev}><SwiperPrev width={8} height={12} /></button>
	{/if}

	{#if startPage > 1}
		<button on:click={() => gotoPage(1)} class:active={currentPage === '1'}>1</button>
		{#if startPage > 2}
			<button disabled>...</button>
		{/if}
	{/if}

	{#each Array(endPage - startPage + 1) as _, i (i + startPage)}
		<button
			class="pages"
			on:click={() => gotoPage(i + startPage)}
			class:active={i + startPage === currentPage}>{i + startPage}</button
		>
	{/each}

	{#if endPage < totalPages}
		{#if endPage < totalPages - 1}
			<button disabled>...</button>
		{/if}
		<button on:click={() => gotoPage(totalPages)} class:active={currentPage === totalPages}
			>{totalPages}</button
		>
	{/if}
	{#if currentPage !== totalPages}
		<button on:click={handleNext}><SwiperNext width={8} height={12} /></button>
	{/if}
</div>

<style lang="scss">
	.pagination {
		display: flex;
		gap: 8px;

		.pages {
			display: flex;
			width: 40px;
			height: 40px;
			border-radius: 6px;
			background: #fff;
			border: 1px solid #d7dbdf;
			justify-content: center;
			align-items: center;

			&.active {
				background-color: var(--blue-color);
				border: none;
				color: #fff;
			}
		}
		button {
			display: flex;
			align-items: center;
			border-radius: 6px;
			background: #fff;
			border: 1px solid #d7dbdf;
			padding: 9px 11px;
			font-size: 14px;
			line-height: 20px;
			color: var(--slate-color);
			gap: 6px;

			&:disabled {
				cursor: default;
			}
		}
	}
</style>
