<script>
	// import { Image } from '@unpic/svelte';

	export let content;

	const extractHeadings = () => {
		const parser = new DOMParser();
		const doc = parser.parseFromString(content.content, 'text/html');

		const headings = doc.querySelectorAll('h1, h2, h3, h4, h5, h6');

		return Array.from(headings).map((heading) => {
			return {
				id: heading.id,
				content: heading.textContent.trim()
			};
			// return heading.textContent.trim();
		});
	};

	const headingArray = extractHeadings();
</script>

<swiper-slide>
	<div class="docs">
		<div class="thumbnail">
			<a href="/docs/{content.id}" target="_blank">
				<!-- <Image
					src={content.thumbnail ? content.thumbnail : '/no-image.png'}
					layout="constrained"
					width={341}
					height={483}
					alt="thumbnail"
				/> -->
				<img src={content.thumbnail ? content.thumbnail : '/no-image.png'} alt="thumbnail" />
			</a>
		</div>
		<div class="list-wrap">
			<ul>
				<li class="chapter">
					<a href="/docs/{content.id}" target="_blank">
						<span>{content.book} {content.chapter.toUpperCase()}</span>
					</a>
				</li>
				{#each headingArray as heading}
					{#if heading.content !== ''}
						<li class="item">
							<a href="/docs/{content.id}#{heading.id}" target="_blank">
								{@html heading.content}
							</a>
						</li>
					{/if}
				{/each}
			</ul>
		</div>
	</div>
</swiper-slide>

<style lang="scss">
	.docs {
		display: flex;
		justify-content: space-between;
		gap: 24px;
		margin-top: 48px;
		.thumbnail {
			width: 341px;
			border-radius: 8px;
			overflow: hidden;
			max-height: 483px;

			img {
				object-fit: cover;
				width: 100%;
				height: 100%;
				display: block;
			}
		}
		.list-wrap {
			flex: 1;
			height: 483px;
			padding-bottom: 65px;

			ul {
				height: 100%;
				overflow: auto;
			}

			.chapter {
				a:hover {
					text-decoration: underline;
					color: #fff;
				}
				span {
					font-weight: 700;
					font-size: 24px;
					line-height: 30px;
					display: block;
					color: #fff;
					padding-left: 60px;
					padding-top: 12px;
					padding-bottom: 12px;
					position: relative;

					&::before {
						content: '';
						position: absolute;
						top: 0;
						bottom: 0;
						margin: auto;
						left: 20px;
						width: 28px;
						height: 28px;
						background-image: url('/book.png');
						background-repeat: no-repeat;
						background-position: center;
					}
				}
			}

			.item a {
				color: #fff;
				font-weight: 500;
				font-size: 16px;
				line-height: 24px;
				padding-top: 14px;
				padding-bottom: 14px;
				padding-left: 60px;
				display: block;
				position: relative;

				&:hover {
					text-decoration: underline;
				}

				&::before {
					content: '';
					position: absolute;
					top: 0;
					bottom: 0;
					margin: auto;
					left: 20px;
					width: 28px;
					height: 28px;
					background-image: url('/page.png');
					background-repeat: no-repeat;
					background-position: center;
				}
			}

			li:nth-child(2) a {
				color: var(--text-color);
				background: #f8f9fa;
				&::after {
					content: '';
					position: absolute;
					left: 0;
					top: 0;
					bottom: 0;
					width: 3px;
					background: var(--blue-color);
				}
			}
		}
	}
</style>
