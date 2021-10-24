<template>
  <transition name="search-card">
    <v-card
      v-if="isShow"
      style="
        position: absolute;
        top: -10px;
        left: 55px;
        padding: 11px 12px;
        color: #686868;
        z-index: 100;
        border-radius: 14px;
        background-color: #fafafa;
      "
      elevation="3"
      :style="`width: ${264}px`"
    >
      <v-row
        v-if="!isLoading && searchRes.length > 0"
        class="d-flex justify-start flex-column"
      >
        <v-col
          v-for="(value, index) in searchRes"
          :key="index"
          style="padding: 0"
          class="select-menu-item"
        >
          <template
            v-if="value.publish_cmp && acceptReporter.includes(value.reporter)"
          >
            <div
              class="d-flex flex-column"
              style="padding: 12px; cursor: pointer"
              @click="
                clickAndMove(
                  `/company/${value.publish_cmp}?reporter=${value.reporter}`
                )
              "
            >
              <span class="font-weight-bold" style="font-size: 14px">{{
                value.publish_cmp
              }}</span>
              <span style="font-size: 12px">{{ value.reporter }}</span>
            </div>
          </template>
          <template v-else-if="acceptReporter.includes(value.name)">
            <div
              class="font-weight-bold"
              style="font-size: 14px; padding: 12px; cursor: pointer"
              @click="clickAndMove(`/?reporter=${value.name}`)"
            >
              {{ value.name }}
            </div>
          </template>
        </v-col>
      </v-row>
      <v-row v-else-if="isLoading">
        <div style="padding: 12px">
          <v-progress-circular
            indeterminate
            color="#0056D2"
          ></v-progress-circular>
        </div>
      </v-row>
      <v-row v-else>
        <div class="font-weight-regular" style="font-size: 14px; padding: 12px">
          검색 결과가 없습니다.
        </div>
      </v-row>
    </v-card>
  </transition>
</template>

<script>
import API from '@/API'
export default {
  props: {
    searchWord: {
      type: String,
      default: '',
    },
    // closeCard: {
    //   type: Boolean,
    //   default: false,
    // },
  },
  data() {
    return {
      isShow: false,
      isLoading: false,
      searchRes: [],
      acceptReporter: API.reporters,
    }
  },
  watch: {
    searchWord() {
      if (this.searchWord !== '') {
        this.showCard()
        this.searchCompanyAndReporter(this.searchWord)
      }
    },

    // closeCard() {
    //   console.log('this.closeCard', this.closeCard)
    //   if (this.closeCard === true) {
    //     console.log('1')
    //     this.isShow = false
    //   } else {
    //     console.log('this.isShow', this.isShow)
    //   }
    // },
  },
  methods: {
    showCard() {
      this.isShow = true
    },
    closeCard() {
      this.isShow = false
    },
    clickAndMove(url) {
      this.closeCard()
      this.$router.push(url)
    },
    async searchCompanyAndReporter(searchWord) {
      this.isLoading = true
      const res = await API.getSearch(searchWord)
      this.searchRes = []
      res.forEach((value) => {
        if (value.reporter) {
          if (API.reporters.includes(value.reporter)) this.searchRes.push(value)
        } else if (value.name) {
          if (API.reporters.includes(value.name)) this.searchRes.push(value)
        }
      })
      this.isLoading = false
      // this.searchRes = await API.getSearch(searchWord)
    },
  },
}
</script>

<style>
.search-card-enter-active,
.search-card-leave-active {
  transition: opacity 0.5s;
}
.search-card-enter, .search-card-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.select-menu-item:hover {
  background-color: #e9e9e9;
}
</style>