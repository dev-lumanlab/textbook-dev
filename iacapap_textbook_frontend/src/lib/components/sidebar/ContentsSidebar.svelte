<script>
	import Toc from '../Toc.svelte';
	import Sidebar from './Sidebar.svelte';

	export let show = false;
	export let thumbnailSrc;
	export let title;
</script>

<Sidebar bind:show title="Contents">
	<div class="content">
		<div class="img-wrap">
			<img src={thumbnailSrc ? thumbnailSrc : '/no-image.png'} alt={`${title} 썸네일`} />
		</div>
		<h2>{title}</h2>
		<div>
			<Toc />
		</div>
	</div>
</Sidebar>

<style lang="scss">
	.content {
		padding: 0 40px;

		h2 {
			font-weight: 700;
			font-size: 20px;
			line-height: 30px;
			color: var(--blue-color);
			padding: 32px 0;
		}

		img {
			width: 100%;
			object-fit: cover;
			aspect-ratio: 4/3;
		}
	}
</style>
