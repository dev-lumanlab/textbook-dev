<script>
	import { AdminDocsCardList, AdminDocsList } from '$lib/components/docs';
	import Tabs from '$lib/components/Tabs.svelte';
	import { page } from '$app/stores';
	import Pagination from '$lib/components/Pagination.svelte';
	import { deleteSavedArticle, postPublishingArticle } from '$lib/api/docs';
	import DeleteAlert from '$lib/components/modal/DeleteAlert.svelte';
	import { goto, invalidateAll } from '$app/navigation';
	import SearchInput from '$lib/components/input/SearchInput.svelte';
	import PublishingConfirmCancelAlert from '$lib/components/modal/PublishingConfirmCancelAlert.svelte';

	export let data;

	let isDeleteModalOpen = false;
	let isPublishingModalOpen = false;
	let deleteId = null;
	let publishingId = null;
	let searchValue = '';

	$: contents = data.contents;
	$: limit = data.limit; // 한 페이지에 보여줄 아이템 수
	$: tabs = $page.params.tabs;
	$: total = data.total; // 서버에서 전달받은 총 데이터 개수
	$: totalPages = Math.ceil(total / limit); // 전체 페이지 수

	const openDeleteModal = (id) => {
		isDeleteModalOpen = true;
		deleteId = id;
	};

	const closeDeleteModal = () => {
		isDeleteModalOpen = false;
	};

	const openPublishingModal = (id) => {
		isPublishingModalOpen = true;
		publishingId = id;
	};

	const closePublishingModal = () => {
		isPublishingModalOpen = false;
	};

	const onDonePublishing = async () => {
		if (publishingId) {
			const response = await postPublishingArticle(publishingId);
			if (response.status === 200) {
				invalidateAll();
				closePublishingModal();
			}
		}
	};

	const onDelete = async () => {
		if (deleteId) {
			const response = await deleteSavedArticle(deleteId);
			if (response.status === 200) {
				invalidateAll();
				closeDeleteModal();
			}
		}
	};

	const onSearch = async () => {
		if (searchValue) {
			goto(`?search=${searchValue}`);
		} else {
			goto($page.url.pathname);
		}
	};
</script>

<svelte:head>
	<title>Save List - IACAPAP</title>
</svelte:head>

<div class="wrap">
	<div class="top">
		<h2>IACAPAP Textbook of Child and Adolescent Mental Health ver2.0</h2>
		<div class="tabs">
			<Tabs bind:tabs />
		</div>
	</div>

	{#if tabs === 'list'}
		<AdminDocsList {contents} onDelete={openDeleteModal} onPublishing={openPublishingModal} />
	{:else}
		<AdminDocsCardList {contents} onDelete={openDeleteModal} onPublishing={openPublishingModal} />
	{/if}

	<div class="bottom">
		<form on:submit|preventDefault={onSearch}>
			<SearchInput bind:value={searchValue} />
		</form>
		<Pagination {totalPages} />
	</div>
</div>
<DeleteAlert isModalOpen={isDeleteModalOpen} onCancel={closeDeleteModal} {onDelete} />
<PublishingConfirmCancelAlert
	isModalOpen={isPublishingModalOpen}
	onCancel={closePublishingModal}
	onDone={onDonePublishing}
/>

<style lang="scss">
	.wrap {
		@include wrap-size();
	}

	.top {
		margin-bottom: 16px;
		position: relative;

		display: flex;
		justify-content: space-between;
		align-items: center;

		h2 {
			font-weight: 700;
			font-size: 24px;
			line-height: 30px;
		}
	}

	.bottom {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-top: 40px;
		margin-bottom: 80px;
	}
</style>
