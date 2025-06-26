import { API } from '$lib/api';
import { writable } from 'svelte/store';

const createDocTab = () => {
	const { subscribe, set, update } = writable('topic');

	/**
	 * `change` 함수는 `tab` 매개변수를 받아서 상태를 변경합니다.
	 * @param {('topic'|'graphics')} tab - 변경할 탭. 'topic' 또는 'graphics'만 허용됩니다.
	 * @returns {Promise<void>} 상태가 성공적으로 변경되면 resolve되는 Promise 객체를 반환합니다.
	 */
	const change = async (tab) => {
		set(tab);
	};

	return {
		subscribe,
		change
	};
};

export const docTabStore = createDocTab();
