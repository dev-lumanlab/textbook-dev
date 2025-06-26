<script>
	/**
	 * @type {'User' | 'Admin'}
	 */
	export let role = 'Admin';
</script>

<div style="background-color: {role === 'User' ? '#F1F3F5' : '#e9f9ee'};" class="badge">
	<span style="color: {role === 'User' ? '#687076' : '#299764'};"><slot /></span>
</div>

<style lang="scss">
	.badge {
		display: inline-block;
		padding: 4px 8px;
		border-radius: 4px;

		span {
			font-weight: 500;
			font-size: 12px;
			line-height: 18px;
		}
	}
</style>
