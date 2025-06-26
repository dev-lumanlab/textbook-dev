<script>
	import { DocsSlide } from '$lib/components/docs';
	import { register } from 'swiper/element/bundle';
	import 'swiper/swiper-bundle.css';
	import '$styles/swiper.scss';
	import { SwiperNext, SwiperPrev } from '$lib/components/icons';
	import { onMount } from 'svelte';

	export let data;

	register();

	let swiperEl;
	let contents = [];

	const goPrev = () => {
		swiperEl.swiper.slidePrev();
	};

	const goNext = () => {
		swiperEl.swiper.slideNext();
	};

	onMount(async () => {
		contents = data.contents;
	});
</script>

<svelte:head>
	<title>IACAPAP</title>
</svelte:head>

<section class="visual">
	<div class="wrap">
		<h2>
			IACAPAP Textbook of<br />
			Child and Adolescent Mental Health <span>ver2.0</span>
		</h2>

		<div class="swiper-wrap">
			<swiper-container allow-touch-move="false" bind:this={swiperEl}>
				{#if contents.length > 0}
					{#each contents as content}
						<DocsSlide {content} />
					{/each}
				{/if}
			</swiper-container>
			<div class="navigation">
				<button class="prev" on:click={goPrev}><SwiperPrev /></button>
				<button class="next" on:click={goNext}><SwiperNext /></button>
			</div>
		</div>
	</div>
</section>
<section class="updates">
	<div class="wrap">
		<article class="update">
			<span class="badge">New</span>
			<h2>new update</h2>
			<p>
				Children psychiatrists<br />
				I'm updating my textbooks every day.
			</p>
			<a href="/new-update">New update view</a>
		</article>
		<article class="highlight">
			<span class="badge">New</span>
			<h2>Check out the highlights</h2>
			<p>
				The important contents of the textbook<br />
				You can highlight it.
			</p>
			<a href="/highlight">Go to see the highlights</a>
		</article>
	</div>
</section>
<section class="trusted">
	<div class="wrap">
		<h2>Trusted by</h2>
		<div class="trusted-logos">
			<div class="left">
				<h3>Sponsored by</h3>
			</div>
			<div class="right">
				<h3>developed by</h3>
			</div>
		</div>
	</div>
</section>

<style lang="scss">
	.wrap {
		@include wrap-size();
	}

	.visual {
		margin-top: -80px;
		padding-top: 80px;
		padding-bottom: 60px;
		position: relative;

		&::before {
			content: '';
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 915px;
			background: linear-gradient(180deg, #1488cc 0%, #2b32b2 100%);
			z-index: -1;
		}

		h2 {
			font-size: 64px;
			line-height: 80px;
			text-align: center;
			font-weight: 500;
			color: #fff;

			span {
				font-size: 32px;
			}
		}
	}

	.updates {
		padding-bottom: 80px;
		.wrap {
			display: flex;
			justify-content: space-between;
			// justify-content: center;
			gap: 24px;
		}

		article {
			border-radius: 16px;
			background: #fff;
			flex: 1;
			// width: 50%;

			padding: 24px;
			background-repeat: no-repeat;

			&.update {
				background-image: url('/update-visual.png');
				background-position: top 136px right 24px;
			}

			&.highlight {
				background-image: url('/highlight-visual.png');
				background-position: top 112px right 24px;
			}

			.badge {
				color: #006cec;
				display: inline-block;
				font-size: 14px;
				line-height: 20px;
				font-weight: 500;
				padding: 6px 10px;
				background: #e8f3ff;
				border-radius: 6px;
				margin-bottom: 16px;
			}

			h2 {
				font-size: 32px;
				line-height: 40px;
				font-weight: 700;
				margin-bottom: 16px;
			}

			p {
				font-size: 16px;
				line-height: 26px;
				font-weight: 500;
				margin-bottom: 40px;
			}

			a {
				display: inline-block;
				font-size: 20px;
				line-height: 30px;
				font-weight: 500;
				color: var(--blue-color);
				padding: 13px 38px 13px 0;
				background-image: url('/arrow-right.png');
				background-position: 100% center;
				background-repeat: no-repeat;
				background-size: auto;
				margin-bottom: 20px;
			}
		}
	}

	.trusted {
		background: #fff;
		padding: 120px 0;

		h2 {
			font-size: 40px;
			line-height: 50px;
			font-weight: 600;
			text-align: center;
		}

		.trusted-logos {
			display: flex;
			justify-content: center;
			margin-top: 60px;

			.left,
			.right {
				padding-left: 72px;
				width: 360px;
			}

			h3 {
				padding-bottom: 90px;
				font-size: 14px;
				line-height: 20px;
				font-weight: 500;
				background-repeat: no-repeat;
				background-position: left 0 bottom 0;
			}

			.left {
				h3 {
					background-image: url('/otsuka.png');
				}
			}

			.right {
				h3 {
					background-image: url('/developed.png');
				}
			}
		}
	}
</style>
