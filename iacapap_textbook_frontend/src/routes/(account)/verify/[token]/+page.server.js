import { error } from '@sveltejs/kit';

export async function load({ params, fetch }) {
	const token = params.token;

	// 사용자 토큰으로 이메일 정보를 가져옵니다.
	const response = await fetch(`/api/auth`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ token })
	});

	const data = await response.json();

	if (response.ok) {
		return {
			...data
		};
	}

	error(404, 'Not found');
}
