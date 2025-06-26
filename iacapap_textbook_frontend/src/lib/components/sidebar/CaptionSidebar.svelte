<script>
	import Sidebar from './Sidebar.svelte';

	export let show = false;
	export let content = '';
</script>

<Sidebar bind:show title="Caption">
	<div class="content">
		<p>
			{content}
		</p>
	</div>
</Sidebar>

<style lang="scss">
	.content {
		padding: 32px;

		p {
			font-size: 24px;
			line-height: 42px;
		}
	}
</style>
