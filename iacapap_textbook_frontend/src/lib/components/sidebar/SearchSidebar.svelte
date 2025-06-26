<script>
	import { Close } from '../icons';
	import Sidebar from './Sidebar.svelte';
	import '$styles/searchContent.scss';
	import { onMount, tick } from 'svelte';

	export let show = false;
	export let content = '';
	let search = '';
	let foundContent = '';
	let inputEl;
	let currentFoundIndex = -1;

	let contentEl;

	$: if (show) {
		tick().then(() => {
			inputEl.focus();
		});
		currentFoundIndex = -1;
	}

	onMount(() => {
		const parser = new DOMParser();
		const doc = parser.parseFromString(content, 'text/html');
		const bodyContent = doc.body.innerHTML;
		content = bodyContent;

		content = removeSpanAndMergeText();
	});

	function removeSpanAndMergeText() {
		const parser = new DOMParser();
		const doc = parser.parseFromString(content, 'text/html');

		const headings = doc.querySelectorAll('h1, h2, h3, h4, h5, h6');

		// h 태그를 선택하여 span 태그를 제거하고 텍스트를 합침
		headings.forEach(function (heading) {
			const text = heading.textContent;
			heading.innerHTML = text.trim();
			if (heading.innerHTML === '') {
				heading.remove();
			}
		});

		// p 태그를 선택하여 span 태그를 제거하고 텍스트를 합침
		const paragraphs = doc.querySelectorAll('p');
		paragraphs.forEach(function (paragraph) {
			const text = paragraph.textContent;
			paragraph.innerHTML = text.trim();
			if (paragraph.innerHTML === '') {
				paragraph.remove();
			}
		});

		const list = doc.querySelectorAll('li');

		list.forEach(function (li) {
			const text = li.textContent;
			li.innerHTML = text.trim();
			if (li.innerHTML === '') {
				li.remove();
			}
		});

		// 수정된 내용을 다시 설정
		const bodyContent = doc.body.innerHTML;
		return bodyContent;
	}

	const onSearch = () => {
		const lowerCaseSearch = search.toLowerCase(); // 검색어를 소문자로 변환
		const headings = content.split(/(?=<h[1-6](?:\s[^>]*)?>)/);

		if (headings[0] === '') {
			headings.shift();
		}

		foundContent = headings.find((heading, index) => {
			const parser = new DOMParser();
			const doc = parser.parseFromString(heading, 'text/html');
			const text = doc.body.textContent;
			if (index >= currentFoundIndex && text.toLowerCase().includes(lowerCaseSearch)) {
				currentFoundIndex = index + 1;
				return true;
			}
			return false;
		});

		if (!foundContent) {
			currentFoundIndex = -1;
			return (foundContent = '');
		}

		foundContent = foundContent.replace(
			new RegExp(`(${search})(?=[^>]*<)`, 'gi'),
			`<mark>$1</mark>`
		);
	};

	const onReset = () => {
		search = '';
		foundContent = '';
	};
</script>

<Sidebar bind:show title="Search">
	<div class="container">
		<form on:submit|preventDefault={onSearch}>
			<div class="search">
				<input type="text" placeholder="Search" bind:this={inputEl} bind:value={search} />
				{#if search}
					<button type="button" class="clear" on:click={onReset}>
						<Close color="#889096" width={12} height={12} />
					</button>
				{/if}
			</div>
		</form>
		<div class="content">
			{#if foundContent}
				<div class="search-content" bind:this={contentEl}>
					{@html foundContent}
				</div>
			{:else}
				<div class="no-found">
					<p>Search a single or sentence.</p>
				</div>
			{/if}
		</div>
	</div>
</Sidebar>

<style lang="scss">
	.container {
		padding: 0 40px 40px 40px;
	}
	.search {
		position: relative;
		border-bottom: 1px solid #dfe3e6;

		input {
			background-image: url('/search3.png');
			background-repeat: no-repeat;
			background-position: 0 center;
			width: 100%;
			border: none;
			padding: 14px 32px 16px 36px;
			font-size: 18px;
			line-height: 26px;

			&:focus {
				outline: none;
			}

			&::placeholder {
				color: var(--slate-base-color);
			}
		}

		.clear {
			right: 0;
			top: 0;
			bottom: 0;
			margin: auto;
			width: 20px;
			height: 20px;
			position: absolute;
			display: flex;
			align-items: center;
			justify-content: center;
		}
	}
	.content {
		margin-top: 40px;

		.no-found {
			text-align: center;
			background-color: #f1f3f5;
			padding: 96px 0 40px;
			background-image: url('/file-search.png');
			background-repeat: no-repeat;
			background-position: center 40px;
			border-radius: 16px;

			p {
				color: var(--slate-base-color);
				font-size: 18px;
				line-height: 26px;
			}
		}
	}
</style>
