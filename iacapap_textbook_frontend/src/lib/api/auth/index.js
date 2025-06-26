import { API } from '$lib/api';

/**
 * 사용자 이메일로 인증 메일을 전송합니다.
 * @param {string} email - 사용자 이메일
 * @param {('signup' | 'password-change')} type - 인증 메일 타입
 * @returns {Promise<Response>}
 */
export const postSendEmail = async (email, type = 'signup') => {
	return await fetch(`/api/auth?email=${email}&type=${type}`);
};

/**
 * 새로운 사용자를 등록합니다.
 * @param {Object} data - 사용자 정보 객체
 * @param {string} data.email - 사용자 이메일
 * @param {string} data.password1 - 사용자 비밀번호
 * @param {string} data.password2 - 사용자 비밀번호 확인
 * @returns {Promise<AxiosResponse>}
 */
export const postSignup = async (data) => {
	return await API.post('/user', data);
};

/**
 * 사용자 비밀번호를 변경합니다.
 * @param {Object} data - 사용자 정보 객체
 * @param {string} data.email - 사용자 이메일
 * @param {string} data.new_password1 - 사용자 비밀번호
 * @param {string} data.new_password2 - 사용자 비밀번호 확인
 * @returns {Promise<AxiosResponse>}
 */
export const patchChangePassword = async (data) => {
	return await API.patch('/user/password', data);
};

/**
 * 이메일로 사용자 정보를 가져옵니다.
 * @param {string} email - 사용자 이메일
 * @returns {Promise<AxiosResponse>}
 */
export const getUser = async (email) => {
	return await API.get(`/user?email=${email}`);
};

/**
 * 이메일로 사용자 정보를 가져옵니다.
 * @param {number} page - 페이지 번호
 * @param {number} limit - 페이지 당 데이터 수
 * @returns {Promise<AxiosResponse>}
 */
export const getUsers = async (page, limit) => {
	return await API.get(`/user?page=${page}&limit=${limit}`);
};

/**
 * 사용자 등급을 수정합니다.
 * @param {string} email
 * @param {number} level
 * @returns
 */
export const patchUserLevel = async (email, level) => {
	return await API.patch(`/user/auth?email=${email}&level=${level}`);
};

/**
 * 사용자를 삭제합니다.
 * @param {string} userId
 * @returns
 */
export const deleteUser = async (userId) => {
	return await API.delete(`/user?user_id=${userId}`);
};
