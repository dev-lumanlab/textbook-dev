<script>
	export let isOpen = false;
</script>

{#if isOpen}
	<div class="modal-overlay">
		<div class="spinner"></div>
	</div>
{/if}

<style>
	.modal-overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.3);
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 9999;
	}

	.spinner {
		background-image: url('/spinner.gif');
		width: 100%;
		height: 100%;
		background-size: 150px;
		background-repeat: no-repeat;
		background-position: center;
	}
</style>
