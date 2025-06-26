<script>
	import { fly } from 'svelte/transition';
	import { Close } from '$lib/components/icons';

	export let show = false;

	/**
	 * @type {"Caption" | "Contents" | "Highlight" | "Search"}
	 */
	export let title;

	let asideElement;

	const closeSidebar = () => {
		show = false;
	};
</script>

{#if show}
	<!-- 접근성 경고 무시 -->
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div class="overlay" on:mousedown|self={closeSidebar}>
		<aside
			bind:this={asideElement}
			transition:fly={{ x: 500, opacity: 1 }}
			class:caption={title === 'Caption'}
		>
			<header>
				<span>
					{title}
				</span>
				<button on:click={closeSidebar}><Close /></button>
			</header>
			<div class="contents">
				<slot />
			</div>
		</aside>
	</div>
{/if}

<style lang="scss">
	.overlay {
		position: fixed;
		top: 0;
		right: 0;
		width: 100%;
		height: 100%;
		z-index: 9999;

		aside {
			cursor: inherit;
			position: absolute;
			background: #fff;
			right: 0;
			top: 0;
			width: 480px;
			height: 100%;
			box-shadow: 0px 25px 50px -12px #0000002e;

			&.caption {
				width: 420px;

				header {
					padding-left: 32px;
					padding-right: 32px;
				}
			}

			header {
				padding-left: 40px;
				padding-right: 40px;
				padding-top: 36.5px;
				padding-bottom: 20.5px;
				display: flex;
				justify-content: space-between;

				span {
					font-weight: 700;
					font-size: 24px;
					line-height: 30px;
					margin-top: 4px;
				}

				button {
					width: 48px;
					height: 48px;
					display: flex;
					align-items: center;
					justify-content: center;
				}
			}
		}
		.contents {
			height: calc(100% - 105px);
			overflow-y: auto;
		}
	}
</style>
