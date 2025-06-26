import { API } from '$lib/api';

/**
 * 저장된 문서를 가져옵니다.
 * @param {number} id - 가져올 문서의 ID
 * @returns {Promise<AxiosResponse>} 저장된 문서 API 응답
 */
export const getSaveArticle = async (id) => {
	return await API.get(`/article/${id}`);
};

/**
 * 게시된 문서를 가져옵니다.
 * @param {number} id - 가져올 문서의 ID
 * @returns {Promise<AxiosResponse>} 게시된 문서 API 응답
 */
// export const getPublishingArticle = async (id) => {
// 	return await API.get(`/article/${id}/publishing`);
// };

/**
 * 저장된 문서 목록을 가져옵니다.
 * @param {number} currentPage - 현재 페이지
 * @param {number} limit - 페이지 당 문서 수
 * @returns {Promise<AxiosResponse>} 게시된 문서 목록 API 응답
 */
export const getSaveArticleList = async (currentPage, limit) => {
	return await API.get(`/article?published=false&page=${currentPage}&limit=${limit}`);
};

/**
 * 게시된 문서 목록을 가져옵니다.
 * @param {number} currentPage - 현재 페이지
 * @param {number} limit - 페이지 당 문서 수
 * @returns {Promise<AxiosResponse>} 게시된 문서 목록 API 응답
 */
export const getPublishingArticleList = async (currentPage, limit) => {
	return API.get(`/article?published=true&page=${currentPage}&limit=${limit}`);
};

/**
 * 게시된 문서를 비게시 합니다.
 * @param {number} articleId - 비게시할 문서의 ID
 * @returns {Promise<AxiosResponse>} 문서 비게시 후 API 응답
 */
export const postUnPublishingArticle = async (articleId) => {
	return await API.patch(`/article/${articleId}/publish?query=false`);
};

/**
 * 새로운 문서를 생성한 후 게시합니다.
 * @param {Object} data - 새로운 문서를 생성하기 위한 데이터
 * @param {string} data.book - 문서의 책 제목
 * @param {string} data.title - 문서의 소제목
 * @param {string} data.content - 문서의 내용
 * @param {number} data.chapter - 문서의 챕터 번호
 * @returns {Promise<AxiosResponse>} 문서 게시 후 API 응답
 */
export const postPublishingArticle = async (articleId) => {
	return await API.patch(`/article/${articleId}/publish?query=true`);
};

/**
 * 새로운 문서를 저장하지만 게시하지는 않습니다.
 * @param {Object} data - 새로운 문서를 생성하기 위한 데이터
 * @param {string} data.book - 문서의 책 제목
 * @param {string} data.title - 문서의 소제목
 * @param {string} data.content - 문서의 내용
 * @param {number} data.chapter - 문서의 챕터 번호
 * @returns {Promise<AxiosResponse>} 문서 저장 후 API 응답
 */
export const postSaveArticle = async (data) => {
	return await API.post('/article', data);
};

/**
 * 문서를 수정합니다.
 * @param {number} articleId - 수정할 문서의 ID
 * @param {Object} data - 수정할 문서의 데이터
 * @param {string} data.book - 문서의 책 제목
 * @param {string} data.title - 문서의 소제목
 * @param {string} data.content - 문서의 내용
 * @param {number} data.chapter - 문서의 챕터 번호
 * @returns {Promise<AxiosResponse>} 문서 수정 후 API 응답
 */
export const patchSaveArticle = async (articleId, data) => {
	return await API.patch(`/article/${articleId}`, data);
};

/**
 * 게시된 문서를 삭제합니다.
 * @param {number} id - 삭제할 게시된 문서의 ID
 * @returns {Promise<AxiosResponse>} 문서 삭제 후 API 응답
 */
export const deletePublishingArticle = async (id) => {
	return await API.delete(`/article/${id}/publishing`);
};

/**
 * 저장된 문서를 삭제합니다.
 * @param {number} id - 삭제할 저장된 문서의 ID
 * @returns {Promise<AxiosResponse>} 문서 삭제 후 API 응답
 */
export const deleteSavedArticle = async (id) => {
	return await API.delete(`/article/${id}`);
};

/**
 * 퍼블리싱된 버전으로 문서를 복구합니다.
 * @param {number} articleId
 * @returns {Promise<AxiosResponse>}
 */
export const revertToPublishedDocument = async (articleId) => {
	return await API.get(`/article/${articleId}/duplicate`);
};

/**
 * 퍼블리싱된 문서를 검색합니다.
 * @param {string} search
 * @param {number} currentPage
 * @param {number} limit
 * @returns {Promise<AxiosResponse>}
 */
export const searchPublishedArticles = async (search, currentPage, limit) => {
	return await API.get(
		`/article/search?keyword=${search}&published=true&page=${currentPage}&limit=${limit}`
	);
};

/**
 * 저장된 문서를 검색합니다.
 * @param {string} search
 * @param {number} currentPage
 * @param {number} limit
 * @returns {Promise<AxiosResponse>}
 */
export const searchSaveArticles = async (search, currentPage, limit) => {
	return await API.get(
		`/article/search?keyword=${search}&published=false&page=${currentPage}&limit=${limit}`
	);
};

/**
 * 하이라이트 목록을 가져옵니다.
 * @param {number} page
 * @param {number} limit
 * @returns {Promise<AxiosResponse>}
 */
export const getHighlightList = async (page, limit) => {
	return await API.get(`/highlight?page=${page}&limit=${limit}`);
};
