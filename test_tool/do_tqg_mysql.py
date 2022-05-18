
import pymysql
import datetime


# 连接数据库
conn = pymysql.connect(host="10.100.216.122", database="tcbiz_ins", user="jfqadml", passwd="Jqv@cl9EML2WDBCk")
cur = conn.cursor()
count = 202204151320000000
for i in range(3):
    orderNo = "TQGJKN" + str(count+i)
    date_time = datetime.date.today()
    # 生成游标对象
    sql_1 = """
    INSERT INTO tcbiz_ins.RepaySchedule ( memberId, orderNo, orderType, totalNum, num, repayStatus, repayType, isOverdue, repayDate, payDate, payAmt, overdueNum, initTotalAmt, initPrincipal, initFee, initAdvanceFee, totalAmt, principal, fee, overdue, latefee, advanceFee, poundage, remainTotalAmt, remainPrincipal, remainFee, remainOverdue, remainLatefee, remainAdvanceFee, waiverFee, waiverAdvanceFee, waiverOverdue, waiverLatefee, waiverPoundage, loanDiscountfee, dayLoanDiscount, payLoanDiscountfee, repayDiscountfee, refundTotalAmt, isFree, discountParty, rotateStatus, deleted, crtTime, uptTime, interestStatus, deferredFlag, compensatoryFund) VALUES ('1278331974', '{0}', 1, 3, 1, 1, 1, false, '{1}', null, 0, 0, 17626, 16620, 1006, 0, 17626, 16620, 1006, 0, 0, 0, 0,  17626, 16220, 1006, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, false, false, 1, false, '2022-04-14 13:07:45', '2022-04-14 14:20:29', 0, false, null);
    """.format(orderNo, date_time)
    sql_2 = """
    INSERT INTO tcbiz_ins.RepaySchedule (memberId, orderNo, orderType, totalNum, num, repayStatus, repayType, isOverdue, repayDate, payDate, payAmt, overdueNum, initTotalAmt, initPrincipal, initFee, initAdvanceFee, totalAmt, principal, fee, overdue, latefee, advanceFee, poundage, remainTotalAmt, remainPrincipal, remainFee, remainOverdue, remainLatefee, remainAdvanceFee, waiverFee, waiverAdvanceFee, waiverOverdue, waiverLatefee, waiverPoundage, loanDiscountfee, dayLoanDiscount, payLoanDiscountfee, repayDiscountfee, refundTotalAmt, isFree, discountParty, rotateStatus, deleted, crtTime, uptTime, interestStatus, deferredFlag, compensatoryFund) VALUES ('1278331974','{0}' , 1, 3, 2, 1, 1, false, '2022-05-15', null, 0, 0, 17626, 16667, 959, 0, 16667, 16667, 0, 0, 0, 0, 0, 16667, 16667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, false, false, 1, false, '2022-04-14 13:07:45', '2022-04-14 13:07:48', 0, false, null);
    """.format(orderNo)
    sql_3 = """
    INSERT INTO tcbiz_ins.RepaySchedule ( memberId, orderNo, orderType, totalNum, num, repayStatus, repayType, isOverdue, repayDate, payDate, payAmt, overdueNum, initTotalAmt, initPrincipal, initFee, initAdvanceFee, totalAmt, principal, fee, overdue, latefee, advanceFee, poundage, remainTotalAmt, remainPrincipal, remainFee, remainOverdue, remainLatefee, remainAdvanceFee, waiverFee, waiverAdvanceFee, waiverOverdue, waiverLatefee, waiverPoundage, loanDiscountfee, dayLoanDiscount, payLoanDiscountfee, repayDiscountfee, refundTotalAmt, isFree, discountParty, rotateStatus, deleted, crtTime, uptTime, interestStatus, deferredFlag, compensatoryFund) VALUES ('1278331974', '{0}', 1, 3, 3, 1, 1, false, '2022-06-14', null, 0, 0, 17626, 16713, 913, 0, 16713, 16713, 0, 0, 0, 0, 0, 16713, 16713, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, false, false, 1, false, '2022-04-14 13:07:45', '2022-04-14 13:07:48', 0, false, null);
    """.format(orderNo)
    sql_4 = """
    INSERT INTO tcbiz_ins.LoanBill ( memberId, orderNo, bizOrderNo, loanAmount, loanDate, isFree, freeNum, interestType, feeRate, rateType, totalNum, payNum, nextRepayDate, overdueNum, orderStatus, isOverdue, cancelFlag, channelType, acctTempId, productTypeCode, logicTime, parentOrderNo, orderType, totalPayAmt, serviceFee, totalInitFee, totalAmt, totalPrincipal, totalFee, totalOverdue, totalLatefee, totalAdvanceFee, totalRepayPoundage, totalRepayDiscountfee, totalLoanDiscountfee, totalDayLoanDiscountfee, totalPayLoanDiscountfee, loanDiscountfeeType, loanDiscountfeeAmt, loanDiscountfeeRate, remainTotalAmt, remainTotalPrincipal, remainTotalFee, remainTotalOverdue, remainTotalLatefee, refundDate, refundTotalAmt, waiverTotalAmt, deleted, crtTime, uptTime, deferredFlag, loanTerm, loanTermUnit, guaranteeCode) VALUES ( '1278331974', '{0}', null, 50000, '2022-03-15', false, 0, 2, 0.0950, 3, 3, 0, '{1}', 0, 1, false, false, 'C001', 420021, 'TQG', '2022-04-14 14:20:29', null, 5, 0, 0, 2878, 51006, 50000, 1006, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0000, 51006, 50000, 1006, 0, 0, null, 0, 0, false, '2022-04-14 13:07:45', '2022-04-14 14:20:29', false, 3, 3, 'A002');
    """.format(orderNo, date_time)

    # SQL语句
    cur.execute(sql_1)
    cur.execute(sql_2)
    cur.execute(sql_3)
    cur.execute(sql_4)
conn.commit()

# 执行SQL语句
# data = cur.fetchall()
# 通过fetchall方法获得数据
# for i in data[:2]:
#     # 打印输出前2条数据
#     print(i)
cur.close()
# 关闭游标
conn.close()
# 关闭连接
