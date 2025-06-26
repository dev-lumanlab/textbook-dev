<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { Card, List } from '$lib/components/icons';
	import { onMount } from 'svelte';

	export let tabs;

	function changeTabs(tab) {
		const url = $page.url.pathname;
		const lastIndex = url.lastIndexOf('/');
		const result = url.substring(0, lastIndex);
		goto(`${result}/${tab}`);
	}
</script>

<div class="tabs">
	<button on:click={() => changeTabs('list')} class:active={tabs === 'list'}
		><List color={tabs === 'list' ? 'white' : '#687076'} /></button
	>
	<button on:click={() => changeTabs('card')} class:active={tabs === 'card'}
		><Card color={tabs === 'card' ? 'white' : '#687076'} /></button
	>
</div>

<style lang="scss">
	.tabs {
		display: flex;
		gap: 10px;

		button {
			width: 56px;
			height: 56px;
			display: flex;
			justify-content: center;
			align-items: center;
			border-radius: 6px;

			&.active {
				background-color: var(--blue-color);
			}
		}
	}
</style>
