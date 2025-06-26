<script>
	import { page } from '$app/stores';
	import DropMenu from '$lib/components/DropMenu.svelte';
	import Footer from '$lib/components/layout/Footer.svelte';
	import { auth } from '../../../stores/auth.js';

	export let data;

	let menuOpen = false;

	const openMenu = () => {
		menuOpen = true;
	};
</script>

<div class="app">
	<header>
		<div class="wrap">
			<nav>
				<h1 class="logo">
					<a href="/">
						<img src="/logo.png" alt="로고" />
					</a>
				</h1>
				<div class="header-container">
					<ul class="menu">
						<li>
							<a
								href="/admin/publishing-list/list"
								class:active={$page.url.pathname.startsWith('/admin/publishing-list')}
								>publishing List<span class="length">{data.publishingTotal}</span></a
							>
						</li>
						<li>
							<a
								href="/admin/save-list/list"
								class:active={$page.url.pathname.startsWith('/admin/save-list')}
								>Save List<span class="length">{data.saveTotal}</span></a
							>
						</li>
						{#if $auth.level === 2}
							<li>
								<a
									href="/admin/members"
									class:active={$page.url.pathname.startsWith('/admin/members')}
									>Members<span class="length">{data.userTotal}</span></a
								>
							</li>
						{/if}

						<li>
							<a class="write" href="/admin/write">Writing</a>
						</li>
					</ul>
					<div class="profile">
						<button class="menu-open" on:click={openMenu}>{$auth.email.substring(0, 2)}</button>
						<DropMenu bind:menuOpen />
					</div>
				</div>
			</nav>
		</div>
	</header>
	<main class="content">
		<slot />
	</main>

	<Footer />
</div>

<style lang="scss">
	.app {
		height: 100%;
		display: flex;
		flex-direction: column;
	}

	.wrap {
		@include wrap-size();
	}

	/** header */
	header {
		background: #fff;
		nav {
			padding: 16px 0;
			display: flex;
			justify-content: space-between;
			align-items: center;
		}

		.logo {
			img {
				width: 145px;
				height: 40px;
			}
		}

		.header-container {
			display: flex;
			align-items: center;
			gap: 32px;

			.menu {
				display: flex;
				gap: 16px;
			}

			.menu li {
				&:first-child {
					margin-right: 8px;
				}
				a {
					// display: block;
					padding: 9px 4px;
					color: var(--slate-color);
					font-size: 20px;
					line-height: 30px;
					font-weight: 500;
					position: relative;

					display: flex;
					align-items: center;
					gap: 6px;
					.length {
						padding: 0 4px;
						border-radius: 100px;
						background-color: var(--blue-color);
						font-size: 12px;
						line-height: 18px;
						color: #fff;
					}

					&.active {
						color: var(--text-color);

						&::before {
							content: '';
							position: absolute;
							bottom: 0;
							left: 0;
							width: 100%;
							height: 2px;
							background: var(--blue-color);
						}
					}

					&.write {
						background: var(--blue-color);
						color: #fff;
						border-radius: 99px;
						font-size: 16px;
						line-height: 24px;
						padding: 12px 20px;
					}
				}
			}

			.profile {
				position: relative;

				button {
					color: #fff;
					font-size: 14px;
					line-height: 20px;
					font-weight: 600;
					border-radius: 100%;
					background: #c1c8cd;
					width: 40px;
					height: 40px;
				}
			}
		}
	}

	.content {
		flex: 1;
		padding-top: 80px;
	}
</style>
