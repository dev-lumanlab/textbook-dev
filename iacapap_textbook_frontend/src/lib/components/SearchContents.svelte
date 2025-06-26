<script>
	export let contents;
	export let markSearch;
	export let observeTarget;
</script>

<div>
	<ul class="list">
		{#each contents as { id, chapter, title, book, searched_content }}
			<li class="item">
				<a href="/docs/{id}">
					<div class="badge">
						<span>{book}</span>
						<span>{chapter}</span>
						<span>{@html title}</span>
					</div>

					<div class="desc">
						<p>{@html searched_content.replaceAll(markSearch, `<mark>${markSearch}</mark>`)}</p>
					</div>
				</a>
			</li>
		{/each}
		<li bind:this={observeTarget}></li>
	</ul>
</div>

<style lang="scss">
	.list {
		display: flex;
		flex-direction: column;
		gap: 24px;
		margin-bottom: 88px;
		.item {
			background-color: #fff;
			border-radius: 16px;
			height: 246px;
			a {
				display: block;
				padding: 40px 48px;

				.badge {
					display: flex;
					align-items: center;
					gap: 16px;
					span {
						padding: 6px 10px;
						background-color: #e9f9ee;
						color: #299764;
						font-size: 14px;
						line-height: 20px;
						font-weight: 500;
						border-radius: 6px;
					}
				}

				.desc {
					margin-top: 24px;
					p {
						font-size: 20px;
						line-height: 34px;

						/* 특정 단위로 텍스트를 자르기 위한 구문 */
						white-space: normal;
						display: -webkit-box;
						-webkit-line-clamp: 3; /* 텍스트를 자를 때 원하는 단위 ex) 3줄 */
						-webkit-box-orient: vertical;
						overflow: hidden;
					}
				}
			}
		}
	}
</style>
