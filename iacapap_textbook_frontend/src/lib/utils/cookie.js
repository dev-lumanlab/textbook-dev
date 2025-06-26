/**
 * 쿠키를 설정하는 함수입니다.
 *
 * @param {string} name - 설정할 쿠키의 이름입니다.
 * @param {string} value - 설정할 쿠키의 값입니다.
 * @param {Object} options - 쿠키 설정 옵션입니다. 기본값은 { path: '/' }입니다.
 * @param {string} options.path - 쿠키의 경로입니다. 기본값은 '/'입니다.
 * @param {Date} options.expires - 쿠키의 만료 날짜입니다. Date 인스턴스여야 합니다.
 * @param {boolean} options.secure - 쿠키의 보안 설정입니다. true면 Secure 플래그가 설정됩니다.
 * @param {number} options['max-age'] - 쿠키의 최대 수명입니다. 초 단위입니다.
 *
 * @example
 * // 'user'라는 이름의 쿠키를 'John'이라는 값으로 설정하고, secure 옵션을 true로, 'max-age'를 3600으로 설정합니다.
 * setCookie('user', 'John', { secure: true, 'max-age': 3600 });
 */
export const setCookie = (name, value, options = {}) => {
	options = {
		path: '/',
		// 필요한 경우, 옵션 기본값을 설정할 수도 있습니다.
		...options
	};

	if (options.expires instanceof Date) {
		options.expires = options.expires.toUTCString();
	}

	let updatedCookie = encodeURIComponent(name) + '=' + encodeURIComponent(value);

	for (let optionKey in options) {
		updatedCookie += '; ' + optionKey;
		let optionValue = options[optionKey];
		if (optionValue !== true) {
			updatedCookie += '=' + optionValue;
		}
	}

	document.cookie = updatedCookie;
};

/**
 * 쿠키를 가져오는 함수입니다.
 * @param {string} name - 가져올 쿠키의 이름입니다.
 * @returns {string|undefined} - 쿠키의 값이 반환됩니다. 해당 이름의 쿠키가 없으면 undefined가 반환됩니다.
 */
export const getCookie = (name) => {
	let matches = document.cookie.match(
		new RegExp('(?:^|; )' + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + '=([^;]*)')
	);
	return matches ? decodeURIComponent(matches[1]) : undefined;
};

/**
 * 쿠키를 삭제하는 함수입니다.
 * @param {string} name - 삭제할 쿠키의 이름입니다.
 */
export const deleteCookie = (name) => {
	setCookie(name, '', {
		'max-age': -1
	});
};
