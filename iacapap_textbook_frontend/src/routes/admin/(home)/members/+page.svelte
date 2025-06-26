<script>
	import { goto, invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import { deleteUser, getUser, getUsers } from '$lib/api/auth';
	import Pagination2 from '$lib/components/Pagination2.svelte';
	import { Trash2 } from '$lib/components/icons';
	import SwiperNext from '$lib/components/icons/SwiperNext.svelte';
	import SwiperPrev from '$lib/components/icons/SwiperPrev.svelte';
	import SearchInput from '$lib/components/input/SearchInput.svelte';
	import { Badge } from '$lib/components/members';
	import LimitSelectMenu from '$lib/components/members/LimitSelectMenu.svelte';
	import SelectMenu from '$lib/components/members/SelectMenu.svelte';
	import DeleteUserAlert from '$lib/components/modal/DeleteUserAlert.svelte';
	import { onMount } from 'svelte';

	let searchValue = '';

	let users = [];
	let total = 0;
	let limit = 10;

	$: totalPages = Math.ceil(total / limit); // 전체 페이지 수

	let deleteUserId = null;

	let isDeleteModalOpen = false;

	$: currentPage = Number($page.url.searchParams.get('page')) || 1;

	const handleLimitChange = (value) => {
		limit = value;
	};

	const getUserList = async (page = 1) => {
		try {
			const response = await getUsers(page, limit);
			users = response.data.content.users;
			total = response.data.content.total;
		} catch (error) {
			console.error(error);
		}
	};

	onMount(() => {
		getUserList();
	});

	$: {
		getUsers(currentPage, limit).then((response) => {
			users = response.data.content.users;
			total = response.data.content.total;
		});
	}

	const onSearchUser = async () => {
		if (searchValue === '') return getUserList();
		try {
			const response = await getUser(searchValue);
			const user = response.data.content.user;
			users = [user];
		} catch (error) {
			users = [];
			console.error(error);
		}
	};

	const getRoleForLevel = (level) => {
		switch (level) {
			case 0:
				return 'User';
			case 1:
				return 'Admin';
			case 2:
				return 'Master';
			default:
				break;
		}
	};

	const onDeleteClick = (userId) => {
		deleteUserId = userId;
		isDeleteModalOpen = true;
	};

	const onDeleteDone = async () => {
		try {
			await deleteUser(deleteUserId);
			getUserList();
			isDeleteModalOpen = false;
			deleteUserId = null;
			invalidateAll();
		} catch (error) {
			console.error(error);
		}
	};

	const closeDeleteModal = () => {
		isDeleteModalOpen = false;
	};

	const gotoPage = (page) => {
		goto(`?page=${page}`);
	};

	const handleNext = () => {
		const nextPage = currentPage + 1;
		if (nextPage > totalPages) {
			gotoPage(totalPages);
		} else {
			gotoPage(nextPage);
		}
	};

	const handlePrev = () => {
		const prevPage = currentPage - 1;
		if (prevPage < 1) {
			gotoPage(1);
		} else {
			gotoPage(prevPage);
		}
	};
</script>

<div class="wrap">
	<div class="header">
		<h2>Users</h2>
		<form on:submit|preventDefault={onSearchUser}>
			<SearchInput bind:value={searchValue} width={320} />
		</form>
	</div>

	<div class="item-list">
		<div class="item-range">{total} items</div>
		<div class="right">
			<div class="item-range-sub">{currentPage}–{currentPage * limit} from {total} items</div>
			<div class="btns">
				<button on:click={handlePrev}><SwiperPrev width={6} height={10} /></button>
				<button on:click={handleNext}><SwiperNext width={6} height={10} /></button>
			</div>
		</div>
	</div>

	<div class="table">
		<table>
			<colgroup>
				<col />
				<col style="width: 80%" />
				<col style="width: 148px" />
				<col style="width: 72px" />
			</colgroup>
			<thead>
				<tr>
					<td><input type="checkbox" /></td>
					<th class="bold">Users</th>
					<th class="slate" colspan="2">Status</th>
				</tr>
			</thead>
			<tbody>
				{#each users as user}
					<tr>
						<td><input type="checkbox" /></td>
						<td class="profile">
							<div class="icon" class:user={user.level === 0}>{user.email.substring(0, 2)}</div>
							<div class="email">{user.email}</div>
						</td>
						{#if user.level === 2}
							<td>
								<Badge role={getRoleForLevel(user.level)}>{getRoleForLevel(user.level)}</Badge>
							</td>
						{:else}
							<td><SelectMenu userEmail={user.email} role={getRoleForLevel(user.level)} /></td>
							<td class="center">
								<button on:click={() => onDeleteClick(user.id)}>
									<Trash2 width={16} height={18} />
								</button>
							</td>
						{/if}
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
	<div class="pagination">
		<Pagination2 {totalPages} />
		<LimitSelectMenu bind:limit handleChange={handleLimitChange} />
	</div>
</div>

<DeleteUserAlert isModalOpen={isDeleteModalOpen} closeModal={closeDeleteModal} {onDeleteDone} />

<style lang="scss">
	.wrap {
		@include wrap-size();
		padding-bottom: 96px;
	}

	.header {
		margin-bottom: 24px;
		display: flex;
		justify-content: space-between;
		align-items: center;

		h2 {
			font-size: 20px;
			line-height: 30px;
			font-weight: 600;
		}
	}

	.item-list {
		display: flex;
		justify-content: space-between;
		align-items: center;
		color: var(--slate-color);
		margin-bottom: 8px;
		font-size: 14px;
		line-height: 20px;

		.right {
			display: flex;
			gap: 20px;
			align-items: center;

			.btns {
				display: flex;
				gap: 16px;

				button {
					width: 16px;
					height: 16px;
					display: flex;
					justify-content: center;
					align-items: center;
				}
			}
		}
	}

	.bold {
		font-weight: 500;
	}

	.slate {
		color: var(--slate-color);
	}

	.center {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.table {
		background-color: #fff;
		border: 1px solid #e6e8eb;
		border-radius: 6px;

		table {
			border-collapse: collapse;
			width: 100%;

			th,
			td {
				text-align: left;
				padding: 18px 6px;
				font-size: 14px;
				line-height: 20px;
			}

			tbody {
				tr {
					border-top: 1px solid #e6e8eb;
				}
			}

			.profile {
				display: flex;
				gap: 12px;
				align-items: center;

				.icon {
					width: 32px;
					height: 32px;
					color: #fff;
					font-size: 12px;
					line-height: 18px;
					border-radius: 100%;
					display: flex;
					justify-content: center;
					align-items: center;

					background-color: var(--blue-color);
					&.user {
						background-color: #c1c8cd;
					}
				}
			}

			button {
				width: 20px;
				height: 20px;
				display: flex;
				justify-content: center;
				align-items: center;
			}
		}
	}
	.pagination {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-top: 16px;
	}
</style>
