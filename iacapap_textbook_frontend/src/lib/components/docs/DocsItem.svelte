<script>
	import { dateFormat, dateTimeFormat } from '$lib/utils/dateFormat';

	export let title;
	export let id;
	export let book;
	export let chapter;
	export let date = '';
	export let alignItemsCenter = false;
	export let includeSeconds = false;
</script>

<li>
	<a href="/docs/{id}" class:alignItemsCenter>
		<div class="image"></div>
		<div class="section">
			<h3>{@html title}</h3>
			<p>{book} {chapter}</p>
		</div>
		<div class="date">{includeSeconds ? dateTimeFormat(date) : dateFormat(date)}</div>
	</a>
</li>

<style lang="scss">
	li a {
		display: flex;
		justify-content: space-between;
		padding: 12px 0;
		gap: 12px;

		&.alignItemsCenter {
			align-items: center;
		}

		&:hover {
			.section h3 {
				text-decoration: underline;
			}
		}
	}

	.image {
		width: 28px;
		height: 28px;
		background-image: url('/page.png');
		background-size: contain;
		background-repeat: no-repeat;
	}

	.section {
		flex: 1;

		h3 {
			font-size: 20px;
			line-height: 30px;
		}

		p {
			font-size: 16px;
			line-height: 24px;
			color: var(--slate-base-color);
		}
	}

	.date {
		color: var(--slate-color);
	}
</style>
