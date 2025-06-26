import axios from 'axios';
import { PUBLIC_API_SERVER } from '$env/static/public';
import { getCookie } from '../utils/cookie';

export const API = axios.create({
	baseURL: `${PUBLIC_API_SERVER}`,
	withCredentials: false
});

API.interceptors.request.use(
	function (config) {
		if (typeof window !== 'undefined') {
			config.headers.Authorization = 'Bearer ' + localStorage.getItem('access_token');
			// config.headers.Authorization = 'Bearer ' + getCookie('access_token');
			return config;
		}
	},
	function (error) {
		if (typeof window !== 'undefined') {
			return Promise.reject(error);
		}
	}
);

API.interceptors.response.use(
	function (response) {
		return response;
	},
	function (error) {
		if (typeof window !== 'undefined') {
			if (error.response.status === 401) {
				// 토큰 만료시 에러 로직 처리
				// window.location.href = '/signin';
			}
			return Promise.reject(error);
		}
	}
);
