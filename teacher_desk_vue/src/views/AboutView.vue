<template>
  <div class="about has-text-centered">
    <section class="section">
      <figure class="image is-inline-block">
        <img
          :src="logo"
          style="margin: 0 0 -20px 0; width:169.04px"
        />
      </figure>
      <div class="title is-3 has-text-weight-bold">교사의 책상</div>
      <div class="is-size-4">
        <p>교사의책상은 <span class="has-text-weight-bold has-text-info">‘선생님은 쉽게, 아이들은 재밌게!’</span> 라는 모토를 가지고 만들어졌습니다.</p>
        <p> 저희는 학습 보드게임 자료를 자동으로 만들어 주어 교사에게 더 나은 수업 경험을 제공하고자 합니다.</p>
        <p> 교사의책상은 수업시간 속 선생님의 오아시스가 되고 싶습니다.</p>
      </div>
    </section>
    <section class="section">
      <img :src="avatar" />
      <div class="title is-3 has-text-weight-bold">만든 사람들</div>
      <div class="is-size-4">
        <p class="">초등교사인 태기쌤과 나쌤이 만들었습니다.</p>
        <p>컴퓨터교육과 출신인 태기쌤이 코딩을, 미술교육과 출신인 나쌤이 디자인을 맡았습니다!</p>
      </div>
    </section>
  </div>
</template>

<script>
import logo from "../assets/logo-cropped.svg";
import avatar from "../assets/about-picture.png";

export default {
  data: function () {
    return {
      logo: logo,
      avatar: avatar,
    };
  },
};
</script>