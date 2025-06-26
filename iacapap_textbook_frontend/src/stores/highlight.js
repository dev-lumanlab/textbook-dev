import { API } from '$lib/api';
import { writable } from 'svelte/store';

const createHighlight = () => {
	const { subscribe, set, update } = writable([]);

	/**
	 * 하이라이트 데이터를 가져옵니다.
	 * @param {number} articleId
	 */
	const get = async (articleId) => {
		try {
			const response = await API.get(`/highlight?article_id=${articleId}`);
			if (response.status === 200) {
				const {
					content: { highlights }
				} = response.data;
				set(highlights);
			}
		} catch (error) {
			console.error('하이라이트 데이터를 가져오는 중 오류 발생:', error);
		}
	};

	/**
	 * 하이라이트를 삭제합니다.
	 * @param {number} highlightId
	 */
	const remove = async (highlightId) => {
		try {
			const response = await API.delete(`/highlight?highlight_id=${highlightId}`);
			if (response.status === 200) {
				update((highlights) => highlights.filter((highlight) => highlight.id !== highlightId));
			}
		} catch (error) {
			console.error('하이라이트를 삭제하는 중 오류 발생:', error);
		}
	};

	/**
	 * 하이라이트를 추가합니다.
	 * @param {number} articleId
	 * @param {Object} data
	 * @param {number} data.block - 하이라이트 블록 번호
	 * @param {number} data.start - 하이라이트 시작 위치
	 * @param {number} data.end - 하이라이트 끝 위치
	 * @param {string} data.text - 하이라이트된 텍스트
	 */
	const post = async (articleId, data) => {
		try {
			const response = await API.post(`/highlight?article_id=${articleId}`, data);
			if (response.status === 201) {
				const highlightId = response.data.content.highlight_id;
				update((highlights) => [...highlights, { ...data, id: highlightId }]);
			}
		} catch (error) {
			console.error('하이라이트를 추가하는 중 오류 발생:', error);
		}
	};

	const reset = async () => {
		set([]);
	};

	return {
		subscribe,
		get,
		post,
		reset,
		remove
	};
};

export const highlightStore = createHighlight();
