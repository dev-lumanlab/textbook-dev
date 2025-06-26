import { goto } from '$app/navigation';
import { API } from '$lib/api';
import { deleteCookie, setCookie } from '$lib/utils/cookie';
import { writable } from 'svelte/store';

const user = {
	id: '',
	email: '',
	isAuth: false,
	level: 0
};

const createAuth = () => {
	const { subscribe, set, update } = writable({ ...user });

	const getUser = async () => {
		try {
			const response = await API.get('/user/auth');
			// 임시 코드
			if (response.status === 200) {
				const {
					content: { user }
				} = response.data;
				update((newUser) => ({
					...newUser,
					id: user.id,
					email: user.email,
					isAuth: true,
					level: user.level
				}));
			} else {
				update((user) => ({
					...user,
					isAuth: false
				}));
			}
		} catch (error) {
			console.error('사용자 정보를 가져오는 중 오류 발생:', error);
		}
	};

	const signup = async (requestData) => {
		try {
			const response = await API.post('/user', requestData);
			if (response.status === 201) {
				return true;
			}
		} catch (error) {
			console.error('회원가입 중 오류 발생:', error);
			return false;
		}
	};

	const login = async (requestData) => {
		try {
			const response = await API.post('/user/login', requestData);
			if (response.status === 200) {
				const { content } = response.data;
				localStorage.setItem('access_token', content.access_token);

				await auth.getUser();

				// setCookie('access_token', content.access_token, {
				// secure: true
				// 	'max-age': 3600
				// });

				return true;
			}
		} catch (error) {
			console.error('로그인 중 오류 발생:', error);

			return error.response.status;
		}
	};

	const logout = () => {
		set(user);
		localStorage.removeItem('access_token');
		// deleteCookie('access_token');
		window.location.reload();
	};

	return {
		subscribe,
		getUser,
		signup,
		login,
		logout
	};
};

export const auth = createAuth();
