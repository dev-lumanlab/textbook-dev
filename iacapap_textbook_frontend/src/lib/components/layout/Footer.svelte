<footer>
	<div class="wrap">
		<div class="footer-inner">
			<div class="footer-left">
				<span class="logo">
					<img src="/footer-logo.png" alt="LumanLab 로고" />
				</span>
				<p>Copyright © 2023 LumanLab Inc. All Rights Reserved.</p>
			</div>
			<div class="footer-right">
				<div class="company-profile">
					<ul class="divider">
						<li>루먼랩 주식회사</li>
						<li>대표 임재현</li>
						<li>사업자등록번호 : 136-86-02126</li>
					</ul>
				</div>
				<address>
					<p>본사 : 세종특별자치시 조치원읍 군청로 93, SB프라자 601호</p>
					<p>서울지사 : 서울특별시 송파구 법원로11길 11, 문정현대지식산업센터 A동 1513호</p>
					<p>통신판매신고번호 : 제2022-세종조치원-0067 호</p>
				</address>
				<div class="contact-info">
					<ul class="divider">
						<li>+82 02-3400-0297</li>
						<li>info@lumanlab.com</li>
					</ul>
				</div>
				<p class="privacy-policy">개인정보처리방침</p>
			</div>
		</div>
	</div>
</footer>

<style lang="scss">
	.wrap {
		@include wrap-size();
	}

	footer {
		background-color: var(--black-color);
		color: #d7dbdf;

		.footer-inner {
			padding: 32px 0;
			display: flex;
			justify-content: space-between;

			.footer-left {
				display: flex;
				flex-direction: column;
				justify-content: space-between;

				p {
					font-size: 14px;
					line-height: 24px;
					font-weight: 500;
				}
			}

			.footer-right {
				font-size: 12px;
				line-height: 20px;

				address {
					margin: 4px 0;
				}

				.divider {
					display: flex;
					gap: 17px;

					li {
						position: relative;

						& + li::before {
							content: '';
							width: 1px;
							height: 12px;

							background: #d7dbdf;
							position: absolute;
							left: -9px;
							top: 0;
							bottom: 0;
							margin: auto;
						}
					}
				}
				.privacy-policy {
					font-size: 14px;
					line-height: 20px;
					font-weight: 500;
					color: #e6e8eb;
					margin-top: 48px;
				}
			}
		}
	}
</style>
