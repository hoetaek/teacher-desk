<template>
  <div class="suggestions">
    <section class="section has-text-centered">
      <div class="title is-2">반복적으로 만들고 있는 <br>
        활동지나 학습자료가 있나요?</div>
      <p class="title is-2 has-text-info my-6">저희가 대신 만들어드릴게요!</p>

      <div class="container px-5">
        <textarea
          class="textarea"
          rows="2"
          placeholder="이런 걸 만들어주면 좋겠어요."
        ></textarea>
        <div class="box has-text-right">
          <button
            class="button is-info"
            @click="$router.push('/worksheet')"
          > <span class="icon">
              <i class="fas fa-plus"></i>
            </span><span>남기기</span>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>
<style scoped>
.textarea,
.textarea:focus {
  border: none;
  overflow: auto;
  outline: none;

  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;

  resize: none;

  font-size: 25px;
}

textarea::placeholder {
  font-size: 25px;
}

.container {
  width: 45%;
  border: solid 2px;
  border-radius: 25px;
}

.box {
  box-shadow: none;
}
</style>