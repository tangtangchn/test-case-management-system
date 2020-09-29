<template>
<div class="select-batch">
  <el-select
    v-model="valueBatch"
    filterable
    placeholder="选择或搜索批次名称"
    size="large"
    :change="changeSelection()">
    <el-option
      v-for="item in optionsBatch"
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
      optionsBatch: [],
      valueBatch: ''
    }
  },
  methods: {
    changeSelection: function () {
      // 向兄弟组件【ImportTable】传值
      bus.$emit('newBatch', this.valueBatch)
    }
  },
  created () {
    const self = this
    self.$http({
      method: 'post',
      url: 'http://127.0.0.1:5000/api/batch'
    })
      .then(function (res) {
        console.log(res)
        const dataFromWeb = res.data.response
        // 动态加载下拉框数据
        const dataForOptions = []
        for (let k = 0; k < dataFromWeb.length; k++) {
          const obj = {}
          let temp = dataFromWeb[k].split('|')
          obj.value = temp[1]
          obj.label = temp[1]
          dataForOptions[k] = obj
        }
        self.optionsBatch = dataForOptions
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
</script>
