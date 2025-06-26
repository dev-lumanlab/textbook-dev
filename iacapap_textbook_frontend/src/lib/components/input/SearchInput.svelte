<script>
	export let value = '';
	export let width = 365;
</script>

<div class="search">
	<input style="width: {width}px;" type="text" placeholder="Search" bind:value />
</div>

<style lang="scss">
	.search {
		input {
			background-image: url('/search2.png');
			background-repeat: no-repeat;
			background-position: 12px center;
			width: 365px;
			border-radius: 6px;
			border: 1px solid #d7dbdf;
			padding: 9px 11px 9px 35px;
			font-size: 14px;
			line-height: 20px;

			&::placeholder {
				color: var(--slate-base-color);
			}
		}
	}
</style>
