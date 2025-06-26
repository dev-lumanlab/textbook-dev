import { PUBLIC_API_SERVER } from '$env/static/public';

export const uploadFile = (editor) => {
	editor.plugins.get('FileRepository').createUploadAdapter = function (loader) {
		return {
			upload: function () {
				return loader.file.then(
					(file) =>
						new Promise((resolve, reject) => {
							const formData = new FormData();
							formData.append('upload', file);

							fetch(`${PUBLIC_API_SERVER}/article/image/image`, {
								method: 'POST',
								headers: {
									'X-CSRF-TOKEN': 'CSRF-Token',
									Authorization: `Bearer ${localStorage.getItem('access_token')}`
								},
								body: formData
							})
								.then((response) => {
									if (!response.ok) {
										throw new Error('Failed to upload image');
									}
									return response.json();
								})
								.then((data) => {
									// 이미지 업로드가 성공하면 반환된 이미지 URL을 resolve합니다.
									resolve({ default: data.content.url });
								})
								.catch((error) => {
									// 이미지 업로드가 실패하면 에러를 reject합니다.
									reject(error);
								});
						})
				);
			}
		};
	};
};
