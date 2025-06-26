<script>
	import AlertModal from './AlertModal.svelte';

	export let isModalOpen = false;
	export let exit;
	export let saveAndExit;
</script>

<AlertModal isOpen={isModalOpen} bgImage="/exclamation-mark.png">
	<span slot="title">
		There is something in the<br /> process of writing.<br />Would you like to leave?
	</span>
	<span slot="content">
		If you leave the page without saving it, What you've written so far will disappear
	</span>
	<div class="btn-wrap" slot="buttons">
		<button class="btn type2 out" on:click={exit}>out</button>
		<button class="btn type1 save" on:click={saveAndExit}>Save and exit</button>
	</div>
</AlertModal>

<style lang="scss">
	.btn-wrap {
		display: flex;
		justify-content: space-between;
		align-items: center;
		width: 100%;
		gap: 12px;

		.btn {
			width: auto;
		}

		.save {
			flex: 1;
		}
	}

	.btn.type1 {
		font-size: 14px;
		line-height: 20px;
		padding: 10px;
	}
</style>
