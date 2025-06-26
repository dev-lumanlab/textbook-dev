import { EMAIL_ID, EMAIL_PASSWORD } from '$env/static/private';
import { PUBLIC_CLIENT_URL } from '$env/static/public';
import { json } from '@sveltejs/kit';
import nodemailer from 'nodemailer';
import { v4 as uuidv4 } from 'uuid';

// 메모리에 저장할 토큰 객체
const tokens = {};

// 토큰 만료 시간 (예: 1시간)
const tokenExpirationTime = 1 * 60 * 60 * 1000;

// 토큰 만료 처리 함수
const removeExpiredTokens = () => {
	if (Object.keys(tokens).length === 0) {
		// tokens 객체가 비어있으면 함수 실행을 건너뜁니다.
		return;
	}

	const now = new Date().getTime();
	Object.keys(tokens).forEach((token) => {
		if (tokens[token].expiresAt < now) {
			delete tokens[token];
		}
	});
};

const HTML_CONTENTS = (token) => `
<div>
  <div style="padding: 48px 48px 32px 48px; width: 720px; margin: 0 auto">
    <div
      style="
        width: 145px;
        height: 40px;
        margin-bottom: 24px;
        background-repeat: no-repeat;
        background-image: url('${PUBLIC_CLIENT_URL}/logo.png');
				background-size: 100%;
      "
    ></div>
    <h2 style="color: #273645; font-size: 24px; font-weight: 700; line-height: 36px; margin-bottom: 24px">
      Please complete the email authentication!
    </h2>
    <p style="margin-bottom: 42px">
      Thank you for joining us <br />Click the button below to authenticate the email.<br />If you don't authentication,
      your account is not created.
    </p>
    <div style="text-align: center">
      <a
        href="${PUBLIC_CLIENT_URL}/verify/${token}"
        style="
          text-decoration: none;
          background-color: #308fff;
          color: #fff;
          border-radius: 99px;
          padding: 12px 20px;
          font-size: 16px;
          font-weight: 500;
        "
      >
        Check email address
      </a>
    </div>
    <div
      style="
        background-color: #f1f3f5;
        text-align: center;
        font-size: 14px;
        line-height: 20px;
        margin-top: 56px;
        padding: 40px 0;
      "
    >
      <p style="color: #687076; margin: 0">This e-mail is dedicated to sending Luman Lab.</p>
      <p style="color: #889096; margin: 0">Copyright © 2023 LumanLab Inc. All Rights Reserved.</p>
    </div>
  </div>
</div>

`;

// 이메일 전송 함수
const sendEmail = async (email, token) => {
	const transporter = nodemailer.createTransport({
		service: 'Gmail',
		auth: {
			user: EMAIL_ID, // 보내는 이메일 주소
			pass: EMAIL_PASSWORD // 보내는 이메일 비밀번호
		}
	});

	const mailOptions = {
		from: EMAIL_ID, // 보내는 이메일 주소
		to: email,
		subject: 'Please complete the email authentication!',
		html: HTML_CONTENTS(token)
	};

	try {
		await transporter.sendMail(mailOptions);
		console.log('Email sent');
	} catch (error) {
		console.error(error);
	}
};

// 이메일 인증 요청 핸들러
export const GET = async ({ url }) => {
	const email = url.searchParams.get('email');
	const type = url.searchParams.get('type');
	if (!email) {
		return new Response('Invalid email', { status: 400 });
	}

	const token = uuidv4();
	const expiresAt = new Date().getTime() + tokenExpirationTime; // 토큰 만료 시간 설정
	tokens[token] = { email, type, expiresAt }; // 토큰, 이메일, 만료시간 저장

	await sendEmail(email, token);
	return new Response('이메일 인증 링크가 전송되었습니다.');
};

// 이메일 인증 처리 핸들러
export const POST = async ({ request }) => {
	const { token } = await request.json();
	const tokenData = tokens[token]; // 토큰 데이터 조회

	if (tokenData) {
		const { email, type } = tokenData;
		const response = json({ email, type, message: `${email}님의 이메일이 인증되었습니다.` });

		// delete tokens[token]; // 사용한 토큰은 삭제

		return response;
	} else {
		return json({ message: '유효하지 않은 인증 링크입니다.' }, { status: 400 });
	}
};

// 정기적으로 만료된 토큰을 제거하는 함수 실행
setInterval(removeExpiredTokens, 60 * 5000); // 5분마다 실행
