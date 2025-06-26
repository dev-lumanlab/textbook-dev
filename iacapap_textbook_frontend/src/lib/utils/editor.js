import { v4 as uuidv4 } from 'uuid';

export function addUUIDToHeadings(editorContent) {
	// CKEditor에서 사용하는 DOMParser 객체 생성
	const parser = new DOMParser();
	const doc = parser.parseFromString(editorContent, 'text/html');

	// 헤딩 요소를 선택하여 UUID를 추가
	const headings = doc.querySelectorAll('h1, h2, h3, h4, h5, h6');
	headings.forEach(function (heading) {
		// 이미 id가 있는 경우 건너뜀
		if (heading.id) {
			return;
		}

		if (heading.textContent.trim() === '') {
			const replacementParagraph = doc.createElement('p');
			heading.parentNode.replaceChild(replacementParagraph, heading);
		}

		// UUID 생성
		const uuid = uuidv4();

		// heading 요소에 id 속성 추가
		heading.setAttribute('id', uuid);
	});

	const bodyContent = doc.body.innerHTML;
	return bodyContent;
}
