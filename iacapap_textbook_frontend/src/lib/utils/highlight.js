/**
 * 현재 선택된 범위(Range)를 반환하는 함수
 * @returns {Range|null} 선택된 범위 객체 또는 null
 */
const getSelection = () => {
	const selection = window.getSelection();
	if (selection.rangeCount > 0) {
		return selection.getRangeAt(0);
	}
	return null;
};

/**
 * 주어진 범위의 공통 조상 노드를 반환하는 함수
 * @param {Range} range 범위 객체
 * @returns {Node} 공통 조상 노드
 */
const getCommonAncestor = (range) => {
	let commonAncestor = range.commonAncestorContainer;
	if (commonAncestor.nodeType === Node.TEXT_NODE) {
		commonAncestor = commonAncestor.parentNode;
	}
	return commonAncestor;
};

const isValidSelection = (selection) => {
	return selection && selection.toString().length > 0;
};

/**
 * 주어진 컨테이너와 노드 간의 글로벌 오프셋을 계산하는 함수
 * @param {Node} container 컨테이너 노드
 * @param {Node} node 대상 노드
 * @returns {number} 글로벌 오프셋 값
 */
const getGlobalOffset = (container, node) => {
	let offset = 0;
	let child = container.firstChild;

	while (child && child !== node) {
		if (isTextOrElement(child)) {
			offset += child.textContent.length;
		}
		child = child.nextSibling;
	}
	return offset;
};

/**
 * 주어진 노드가 텍스트 노드 또는 요소 노드인지 확인하는 함수
 * @param {Node} node 노드 객체
 * @returns {boolean} 노드가 텍스트 노드 또는 요소 노드인지 여부
 */
const isTextOrElement = (node) => {
	const nodeType = node.nodeType;
	return nodeType === Node.TEXT_NODE || nodeType === Node.ELEMENT_NODE;
};

/**
 * 현재 선택된 텍스트와 그 범위의 시작과 끝 오프셋을 반환하는 함수
 * @returns {Object|null} 선택된 텍스트와 오프셋 정보를 포함하는 객체 또는 null
 */
export const getSelectedTextInfo = () => {
	const selection = window.getSelection();

	if (selection && selection.toString().length > 0) {
		const selectedText = selection.toString();
		return selectedText;
	}
	return null;
};

export const getBlocks = (textContainer) => {
	return textContainer.querySelectorAll('p, h1, h2, h3, h4, li');
};

/**
 * 선택된 텍스트가 포함된 블록 요소의 인덱스를 가져오는 함수
 * @param {textContainer} textContainer 노드 객체
 * @returns {number} 블록 요소의 인덱스
 */
export const findBlockIndex = (textContainer) => {
	const range = getSelection();
	if (isValidSelection(range)) {
		const commonAncestor = getCommonAncestor(range);
		const blocks = getBlocks(textContainer);
		for (let i = 0; i < blocks.length; i++) {
			if (blocks[i] === commonAncestor || blocks[i].contains(commonAncestor)) {
				return i;
			}
		}
	}
};

/**
 * 선택된 텍스트의 전체 시작 오프셋과 끝 오프셋을 계산하는 함수
 * @returns {Object|null} 시작 오프셋과 끝 오프셋 정보를 포함하는 객체 또는 null
 */
export const calculateRelativeOffsets = () => {
	const range = getSelection();
	if (isValidSelection(range)) {
		const commonAncestor = getCommonAncestor(range);
		const start = getGlobalOffset(commonAncestor, range.startContainer) + range.startOffset;
		const end = getGlobalOffset(commonAncestor, range.endContainer) + range.endOffset;

		return {
			start,
			end
		};
	}
};

/**
 * 현재 선택된 범위의 위치와 크기를 계산하여 selectionRect 객체를 업데이트하는 함수
 * @return {Object} selectionRect 위치와 크기 정보를 저장하는 객체
 */
export const getSelectionRect = () => {
	const range = getSelection();
	if (range) {
		const rect = range.getBoundingClientRect();

		var scrollTop = document.documentElement.scrollTop;
		var absoluteTop = rect.top + scrollTop;

		return {
			x: rect.left,
			y: absoluteTop,
			width: rect.width,
			height: rect.height
		};
	} else {
		return null;
	}
};
