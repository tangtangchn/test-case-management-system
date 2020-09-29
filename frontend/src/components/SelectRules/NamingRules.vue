<template>
  <div class="select-area">
    <div class="div-li"><span><strong>首先，请完成以下5个必选项：</strong></span></div>
    <div class="div-li">
      <span><span class="highlight-red">*</span>&nbsp;<strong>产品编号</strong>&nbsp;</span>
      <selectproduct class="select-inline"></selectproduct>
    </div>
    <div class="div-li">
      <span><span class="highlight-red">*</span>&nbsp;<strong>批次名称</strong>&nbsp;</span>
      <selectbatch class="select-inline"></selectbatch>
    </div>
    <div class="div-li">
      <span><span class="highlight-red">*</span>&nbsp;<strong>测试类型</strong>&nbsp;</span>
      <selecttesttype class="select-inline"></selecttesttype>
    </div>
    <div class="div-li">
      <span><span class="highlight-red">*</span>&nbsp;<strong>轮次编号</strong>&nbsp;</span>
      <selectround class="select-inline"></selectround>
    </div>
    <div class="div-li">
      <span><span class="highlight-red">*</span>&nbsp;<strong>执行结果</strong>&nbsp;</span>
      <selectpf class="select-inline"></selectpf>
    </div>
</div>
</template>

<script>
import SelectProduct from '@/components/SelectRules/components/SelectProduct'
import SelectBatch from '@/components/SelectRules/components/SelectBatch'
import SelectTestType from '@/components/SelectRules/components/SelectTestType'
import SelectRoundID from '@/components/SelectRules/components/SelectRoundID'
import SelectPF from '@/components/SelectRules/components/SelectPF'

export default {
  components: {
    'selectproduct': SelectProduct,
    'selectbatch': SelectBatch,
    'selecttesttype': SelectTestType,
    'selectround': SelectRoundID,
    'selectpf': SelectPF
  },
  data () {
    return {
      // pass
    }
  }
}
</script>

<style>
.select-area {
  width: 320px;
  height: 320px;
  border: 1px solid #EFF2F7;
  background-color: #F9FAFC;
  font-size: 15px;
}
.div-li {
  margin-top: 15px;
}
.select-inline {
  display: inline;
}
.highlight-red {
  color: red;
}
</style>
