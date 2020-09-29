<template>
  <div class="select-product">
    <el-select
      v-model="valueProduct"
      filterable
      placeholder="选择或搜索产品编号"
      size="large"
      :change="changeSelection()">
      <el-option
        v-for="item in optionsProduct"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
  </div>
</template>

<script>
import bus from '@/assets/eventBus'

export default {
  data () {
    return {
      optionsProduct: [],
      valueProduct: ''
    }
  },
  methods: {
    changeSelection: function () {
      // 向兄弟组件【ImportTable】传值
      bus.$emit('newProduct', this.valueProduct)
    }
  },
  created () {
    const self = this
    self.$http({
      method: 'post',
      url: 'http://127.0.0.1:5000/api/product'
    })
      .then(function (res) {
        console.log(res)
        const dataFromWeb = res.data.response
        // 动态加载下拉框数据
        const dataForOptions = []
        for (let k = 0; k < dataFromWeb.length; k++) {
          const obj = {}
          obj.value = dataFromWeb[k]
          obj.label = dataFromWeb[k]
          dataForOptions[k] = obj
        }
        self.optionsProduct = dataForOptions
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
</script>
