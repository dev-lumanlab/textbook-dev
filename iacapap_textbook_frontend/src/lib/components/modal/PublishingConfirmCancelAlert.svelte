<script>
	import AlertModal from './AlertModal.svelte';

	export let isModalOpen = false;
	export let onCancel;
	export let onDone;
</script>

<AlertModal isOpen={isModalOpen} bgImage="/AssetonShape2.png">
	<span slot="title">Publishing</span>
	<span slot="content">
		Press the button below to publish. If you don't want to, press the cancel button.
	</span>
	<div class="btn-wrap" slot="buttons">
		<button class="btn type2 cancel" on:click={onCancel}>Cancel</button>
		<button class="btn type1 done" on:click={onDone}>Publishing</button>
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

		.done {
			flex: 1;
		}
	}

	.btn.type1 {
		font-size: 14px;
		line-height: 20px;
		padding: 10px;
	}
</style>
