<script>
	import {
		CaptionSidebar,
		ContentsSidebar,
		HighlightSidebar,
		SearchSidebar
	} from '$lib/components/sidebar';
	import { Download, Caption, Contents, Highlight, Search, Print } from '$lib/components/icons';
	import html2canvas from 'html2canvas';
	import jsPDF from 'jspdf';
	import { docTabStore } from '$stores/docTab.js';
	import '$styles/editor.scss';

	export let data;

	let isCaptionSidebarOpen = false;
	let isContentsSidebarOpen = false;
	let isSearchSidebarOpen = false;
	let isHighlightSidebarOpen = false;

	const openCaptionSidebar = () => {
		isCaptionSidebarOpen = true;
	};

	const openContentsSidebar = () => {
		isContentsSidebarOpen = true;
	};

	const openSearchSidebar = () => {
		isSearchSidebarOpen = true;
	};

	const openHighlightSidebar = () => {
		isHighlightSidebarOpen = true;
	};

	const savePDF = () => {
		const capture = document.getElementById('capture');

		html2canvas(capture, { useCORS: true })
			.then((canvas) => {
				const imgData = canvas.toDataURL('image/png');
				const pdf = new jsPDF('p', 'mm', 'a4');
				const imgProps = pdf.getImageProperties(imgData);
				const pdfWidth = pdf.internal.pageSize.getWidth();
				const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;

				pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
				pdf.save('IACAPAP.pdf');
			})
			.catch((error) => {
				console.error(error);
			});
	};
</script>

<div class="app">
	<header>
		<div class="wrap">
			<div class="left">
				<ul class="menu">
					<li>
						<button on:click={openContentsSidebar}><Contents /><span>Contents</span></button>
					</li>
					<li><button on:click={openSearchSidebar}><Search /><span>Search</span></button></li>
					<li>
						<button on:click={openHighlightSidebar}><Highlight /><span>Highlight</span></button>
					</li>
					<!-- <li><button on:click={openCaptionSidebar}><Caption /><span>Caption</span></button></li> -->
				</ul>
			</div>
			<div class="right">
				<div class="action-buttons">
					<button on:click={savePDF}><Download /></button>
					<button on:click={() => print()}><Print /></button>
				</div>
				<div class="tab">
					<button
						class:active={$docTabStore === 'topic'}
						on:click={() => docTabStore.change('topic')}
					>
						Topic
					</button>
					<button
						class:active={$docTabStore === 'graphics'}
						on:click={() => docTabStore.change('graphics')}
					>
						Graphics
					</button>
				</div>
			</div>
		</div>
	</header>
	<main>
		<slot />
	</main>
</div>

<!-- <CaptionSidebar bind:show={isCaptionSidebarOpen} content="" /> -->
{#if data.content}
	<ContentsSidebar
		bind:show={isContentsSidebarOpen}
		title={data.content.title}
		thumbnailSrc={data.content.thumbnail}
	/>
	<SearchSidebar bind:show={isSearchSidebarOpen} content={data.content.content} />
{/if}
<HighlightSidebar bind:show={isHighlightSidebarOpen} />

<style lang="scss">
	.app {
		// display: flex;
		// flex-direction: column;
		// height: 100%;

		main {
			// flex: 1;
			background: #fff;
		}
	}

	.wrap {
		padding: 24px;
	}

	header {
		background: #fff;
		border-bottom: 1px solid #d7dbdf;
		position: sticky;
		top: 0;
		z-index: 999;

		.wrap {
			display: flex;
			justify-content: space-between;
			align-items: center;
		}

		.left {
			.menu {
				display: flex;

				button {
					font-size: 20px;
					line-height: 30px;
					font-weight: 500;
					padding: 13px 20px 13px 20px;
					color: var(--slate-color);
					display: flex;
					align-items: center;
					gap: 10px;
				}
			}
		}

		.right {
			display: flex;
			gap: 16px;
			align-items: center;

			.action-buttons {
				display: flex;
				gap: 10px;

				button {
					display: flex;
					align-items: center;
					justify-content: center;
					width: 56px;
					height: 56px;
				}
			}

			.tab {
				outline: 1px solid #e6e8eb;
				background: #f1f3f5;
				padding: 4px;
				border-radius: 6px;
				display: flex;

				button {
					width: 168.5px;
					height: 40px;
					color: var(--slate-color);
					font-size: 14px;
					line-height: 20px;
					font-weight: 500;

					&.active {
						background: #fff;
						border-radius: 6px;
					}
				}
			}
		}
	}
</style>
