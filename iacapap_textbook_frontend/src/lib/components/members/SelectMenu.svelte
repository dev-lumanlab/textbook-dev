<script>
	import { onDestroy, onMount } from 'svelte';
	import Badge from './Badge.svelte';
	import { patchUserLevel } from '$lib/api/auth';

	/**
	 * @type {'User' | 'Admin'}
	 */
	export let role = 'Admin';
	export let userEmail;

	let selectEl;
	let optionsEl;

	let isOpen = false;

	const toggle = () => {
		isOpen = !isOpen;
	};

	const handleChange = async (option) => {
		try {
			let level = option === 'Admin' ? 1 : 0;
			const response = await patchUserLevel(userEmail, level);
			role = option;
			toggle();
		} catch (error) {
			console.error(error);
		}
	};

	const handleWindowClick = (event) => {
		const target = event.target;
		if (!selectEl.contains(target) && !optionsEl.contains(target)) {
			isOpen = false;
		}
	};

	onMount(() => {
		window.addEventListener('click', handleWindowClick);
	});

	onDestroy(() => {
		window.removeEventListener('click', handleWindowClick);
	});
</script>

<div class="overlay">
	<button class="select" bind:this={selectEl} class:open={isOpen} on:click={toggle}
		><Badge {role}><div class="dropdown">{role}</div></Badge></button
	>
	<ul class="options" bind:this={optionsEl}>
		<li><button on:click={() => handleChange('Admin')}>Admin</button></li>
		<li><button on:click={() => handleChange('User')}>User</button></li>
	</ul>
</div>

<style lang="scss">
	.overlay {
		position: relative;
		display: inline-block;
	}

	.dropdown {
		padding-right: 18px;
		background-image: url('/arrow-down.png');
		background-repeat: no-repeat;
		background-position: right 0 center;
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
