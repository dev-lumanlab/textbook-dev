<script>
	import { onDestroy, onMount } from 'svelte';
	import Badge from './Badge.svelte';
	import { patchUserLevel } from '$lib/api/auth';

	/**
	 * @type {'User' | 'Admin'}
	 */
	export let limit;
	export let handleChange;

	let selectEl;
	let optionsEl;

	let isOpen = false;

	let options = [10, 20, 30, 40, 50];

	const toggle = () => {
		isOpen = !isOpen;
	};

	const handleWindowClick = (event) => {
		const target = event.target;
		if (!selectEl.contains(target) && !optionsEl.contains(target)) {
			isOpen = false;
		}
	};

	const onClick = (option) => {
		handleChange(option);
		isOpen = false;
	};

	onMount(() => {
		window.addEventListener('click', handleWindowClick);
	});

	onDestroy(() => {
		window.removeEventListener('click', handleWindowClick);
	});
</script>

<div class="overlay">
	<button class="select" bind:this={selectEl} class:open={isOpen} on:click={toggle}>
		<div class="dropdown">Show Items: <span>{limit}</span></div>
	</button>
	<ul class="options" bind:this={optionsEl}>
		{#each options as option}
			<li><button on:click={() => onClick(option)}>{option}</button></li>
		{/each}
	</ul>
</div>

<style lang="scss">
	.overlay {
		position: relative;
		display: inline-block;
	}

	.select {
		background-color: #fff;
		border: 1px solid #d7dbdf;
		padding: 10px 12px 10px 12px;
		border-radius: 6px;
	}

	.dropdown {
		padding-right: 30px;
		background-image: url('/arrow-down.png');
		background-repeat: no-repeat;
		background-position: right 0 center;
		color: var(--slate-color);

		span {
			color: var(--black-color);
		}
	}

	.options {
		position: absolute;
		top: calc(100% + 2px);
		width: 100%;
		display: none;
		border-radius: 6px;
		background-color: #fff;
		padding: 4px 0;
		outline: 1px solid #eceef0;
		z-index: 100;

		li {
			button {
				width: 100%;
				padding: 10px 12px;
				text-align: left;
				background-color: #fff;
				font-size: 14px;
				line-height: 20px;
				color: #333;
				font-size: 14px;
				line-height: 20px;

				&:hover {
					background: #f1f3f5;
				}
			}
		}
	}

	.select.open + .options {
		display: block;
	}
</style>
