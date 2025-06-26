<script>
	import { page } from '$app/stores';
	import DropMenu from '$lib/components/DropMenu.svelte';
	import Footer from '$lib/components/layout/Footer.svelte';
	import { auth } from '../../stores/auth';

	let menuOpen = false;

	const openMenu = () => {
		menuOpen = true;
	};

	const links = [
		{ href: '/search', text: 'Search' },
		{ href: '/new-update', text: 'New update' },
		{ href: '/highlight', text: 'Highlight' }
	];
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
						{#each links as link}
							<li>
								<a href={link.href} class:active={link.href === $page.url.pathname}>
									{link.text}
								</a>
							</li>
						{/each}
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
		{#if $page.url.pathname === '/'}
			<slot />
		{:else}
			<div class="wrap">
				<slot />
			</div>
		{/if}
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
			width: 145px;
			height: 40px;
			img {
				width: 100%;
				height: 100%;
				display: block;
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

			.menu li a {
				display: block;
				padding: 13px 20px;
				color: var(--slate-color);
				font-size: 20px;
				line-height: 30px;
				font-weight: 500;

				&.active {
					color: var(--text-color);
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
					background: #308fff;
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
