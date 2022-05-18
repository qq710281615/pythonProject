
import pymysql
import datetime


# 连接数据库
conn = pymysql.connect(host="10.100.216.122", database="tcbiz_ins", user="jfqadml", passwd="Jqv@cl9EML2WDBCk")
cur = conn.cursor()
count = 202204152036000000
for i in range(300):
    orderNo = "TQYJKN" + str(count+i)
    date_time = str(datetime.date.today()+datetime.timedelta(days=-1))
    date_time_t = str(datetime.date.today())
    print(orderNo)
            # 生成游标对象
    sql_1 = """
        INSERT INTO tcbiz_ins.RepaySchedule ( memberId, orderNo, orderType, totalNum, num, repayStatus, repayType, isOverdue, repayDate, payDate, payAmt, overdueNum, initTotalAmt, initPrincipal, initFee, initAdvanceFee, totalAmt, principal, fee, overdue, latefee, advanceFee, poundage, remainTotalAmt, remainPrincipal, remainFee, remainOverdue, remainLatefee, remainAdvanceFee, waiverFee, waiverAdvanceFee, waiverOverdue, waiverLatefee, waiverPoundage, loanDiscountfee, dayLoanDiscount, payLoanDiscountfee, repayDiscountfee, refundTotalAmt, isFree, discountParty, rotateStatus, deleted, crtTime, uptTime, interestStatus, deferredFlag, compensatoryFund) VALUES ('1251863783', '{0}', 1, 3, 1, 1, 1, true, '{1}', null, 0, 1, 17321, 16346, 975, 0, 16347, 16346, 0, 1, 0, 0, 0, 16347, 16346, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, false, false, 1, false, '2022-04-15 12:10:52', '2022-04-15 12:17:36', 0, false, null);
        """.format(orderNo, date_time)
    sql_2 = """
        INSERT INTO tcbiz_ins.RepaySchedule (memberId, orderNo, orderType, totalNum, num, repayStatus, repayType, isOverdue, repayDate, payDate, payAmt, overdueNum, initTotalAmt, initPrincipal, initFee, initAdvanceFee, totalAmt, principal, fee, overdue, latefee, advanceFee, poundage, remainTotalAmt, remainPrincipal, remainFee, remainOverdue, remainLatefee, remainAdvanceFee, waiverFee, waiverAdvanceFee, waiverOverdue, waiverLatefee, waiverPoundage, loanDiscountfee, dayLoanDiscount, payLoanDiscountfee, repayDiscountfee, refundTotalAmt, isFree, discountParty, rotateStatus, deleted, crtTime, uptTime, interestStatus, deferredFlag, compensatoryFund) VALUES ('1251863783', '{0}', 1, 3, 2, 1, 1, false, '2022-06-15', null, 0, 0, 17321, 16665, 656, 0, 16665, 16665, 0, 0, 0, 0, 0, 16665, 16665, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, false, false, 1, false, '2022-04-15 12:10:52', '2022-04-15 12:10:52', 0, false, null);
        """.format(orderNo)
    sql_3 = """
        INSERT INTO tcbiz_ins.RepaySchedule ( memberId, orderNo, orderType, totalNum, num, repayStatus, repayType, isOverdue, repayDate, payDate, payAmt, overdueNum, initTotalAmt, initPrincipal, initFee, initAdvanceFee, totalAmt, principal, fee, overdue, latefee, advanceFee, poundage, remainTotalAmt, remainPrincipal, remainFee, remainOverdue, remainLatefee, remainAdvanceFee, waiverFee, waiverAdvanceFee, waiverOverdue, waiverLatefee, waiverPoundage, loanDiscountfee, dayLoanDiscount, payLoanDiscountfee, repayDiscountfee, refundTotalAmt, isFree, discountParty, rotateStatus, deleted, crtTime, uptTime, interestStatus, deferredFlag, compensatoryFund) VALUES ('1251863783', '{0}', 1, 3, 3, 1, 1, false, '2022-07-15', null, 0, 0, 17321, 16989, 332, 0, 16989, 16989, 0, 0, 0, 0, 0, 16989, 16989, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, false, false, 1, false, '2022-04-15 12:10:52', '2022-04-15 12:10:52', 0, false, null);
        """.format(orderNo)
    sql_4 = """
        INSERT INTO tcbiz_ins.LoanBill ( memberId, orderNo, bizOrderNo, loanAmount, loanDate, isFree, freeNum, interestType, feeRate, rateType, totalNum, payNum, nextRepayDate, overdueNum, orderStatus, isOverdue, cancelFlag, channelType, acctTempId, productTypeCode, logicTime, parentOrderNo, orderType, totalPayAmt, serviceFee, totalInitFee, totalAmt, totalPrincipal, totalFee, totalOverdue, totalLatefee, totalAdvanceFee, totalRepayPoundage, totalRepayDiscountfee, totalLoanDiscountfee, totalDayLoanDiscountfee, totalPayLoanDiscountfee, loanDiscountfeeType, loanDiscountfeeAmt, loanDiscountfeeRate, remainTotalAmt, remainTotalPrincipal, remainTotalFee, remainTotalOverdue, remainTotalLatefee, refundDate, refundTotalAmt, waiverTotalAmt, deleted, crtTime, uptTime, deferredFlag, loanTerm, loanTermUnit, guaranteeCode) VALUES ( '1251863783', '{0}', null, 50000, '{1}', false, 0, 2, 0.0950, 3, 3, 0, '{2}', 1, 1, true, false, 'C001', 420002, 'TQY', '2022-04-15 12:17:36', null, 1, 0, 0, 1963, 50001, 50000, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0000, 50001, 50000, 0, 1, 0, null, 0, 0, false, '2022-04-15 12:10:52', '2022-04-15 12:17:36', false, 3, 3, null);
        """.format(orderNo, date_time, date_time)

    sql_5 = """INSERT INTO tcbiz_ins.CashOrderInfo ( orderNo, transNo, memberId, dueLoanAmt, realLoanAmt, acctTempId, serviceFee, boundDiscountAmt, activeDiscountAmt, orderState, orderStatus, orderType, productTypeCode, repaymentPeriod, periodType, bankName, idCard, validTime, loanAgreementNo, successTime, successLogicDate, errMsg, deleted, crtTime, updTime, remittanceType, loanPurpose, requestChannel, extAttrs, unionLoanFlag, loanTerm, loanTermUnit, gateId) VALUES ( '{0}', 'XDCL216A86EE5F48485FAAB5BD7A7D530B80', '1251863783', 50000, 50000, 420002, 0, null, 0, '99', 2, true, 'TQY', 3, 2, '建设银行', '2122392242', 1800, null, '2022-04-17 05:30:33', '{1}', null, false, '2022-04-15 12:10:33', '2022-04-15 12:10:58', null, '旅游', 'hybrid', '', false, 3, 3, 'C001');""".format(
        orderNo, date_time)

    sql_6 = """INSERT INTO tcbiz_ins.CashLoanApply ( memberId, orderNo, dueLoanAmt, realLoanAmt, serviceFee, boundDiscountAmt, activeDiscountAmt, loanOrderStatus, productTypeCode, loanNum, interestType, flowStep, bankName, idCard, applyTime, applySuccTime, loanDate, loanEndDate, remittanceType, loanPurpose, remitRefBizId, remitSuccTime, requestChannel, gateId, acctTempId, needSmsConfirm, deleted, crtTime, uptTime, errCode, errMsg, extAttrs, remitAccountType, remitAccountId, encCardNo) VALUES ( '1251863783', '{0}', 50000, 50000, 0, null, 0, true, 'TQY', 3, 2, 'loanSucc', '建设银行', '2122392242', '2022-04-15 12:10:31', '2022-04-15 12:10:51', '2022-04-15', '2022-07-15', null, '旅游', 'XDCL723C8E178F2B4DCDA399D5C230202520', '2022-04-17 05:30:33', 'hybrid', 'C001', 420002, false, false, '2022-04-15 12:10:31', '2022-04-15 12:10:59', null, null, '', 'bankCard', 2122392242, '001427628824478B67FDB3A8A927EE2C3D65EE94671F5E41CF');
    """.format(orderNo)
    sql_7 = """
INSERT INTO tcbiz_ins_yhc.LoanBill ( memberId, orderNo, bizOrderNo, loanAmount, loanDate, isFree, freeNum, interestType, feeRate, rateType, totalNum, payNum, nextRepayDate, overdueNum, orderStatus, isOverdue, cancelFlag, channelType, acctTempId, productTypeCode, logicTime, parentOrderNo, orderType, totalPayAmt, serviceFee, totalInitFee, totalAmt, totalPrincipal, totalFee, totalOverdue, totalLatefee, totalAdvanceFee, totalRepayPoundage, totalRepayDiscountfee, totalLoanDiscountfee, totalDayLoanDiscountfee, totalPayLoanDiscountfee, loanDiscountfeeType, loanDiscountfeeAmt, loanDiscountfeeRate, remainTotalAmt, remainTotalPrincipal, remainTotalFee, remainTotalOverdue, remainTotalLatefee, refundDate, refundTotalAmt, waiverTotalAmt, deleted, crtTime, uptTime, ckStatus, loanTerm, loanTermUnit) VALUES ( '1251863783', '{0}', null, 50000, '{1}', false, 0, 2, 0.0650, 3, 3, 0, '{2}', 1, 1, true, false, 'C001', 420002, 'TQY', '2022-04-15 12:17:36', null, 1, 0, 0, 1963, 50001, 50000, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0000, 50001, 50000, 0, 1, 0, null, 0, 0, false, '2022-04-15 12:10:52', '2022-04-15 12:17:36', null, 3, 3);
""".format(orderNo, date_time, date_time)

    sql_8 = """INSERT INTO tcbiz_ins.LoanBillRates (orderNo, feeValue, feeType, overdueValue, overdueType, latefeeValue, latefeeType, poundageValue, poundageType, serviceFeeValue, serviceFeeType, memberLevel, overduePostponeDay, deleted, crtTime, uptTime, yearVariable, guaranteeRate, guaranteeRateType, originalFeeValue) VALUES ('{0}', '0.065', 3, '1.8', 2, '0', 2, null, 1, '0', 2, 88, '0', false, '2022-04-15 12:10:52', '2022-04-15 12:10:52', null, null, null, '0.065');
    """.format(orderNo)
    sql_9 = """INSERT INTO tcbiz_ins_yhc.LoanBillRates (orderNo, feeValue, feeType, overdueValue, overdueType, latefeeValue, latefeeType, poundageValue, poundageType, serviceFeeValue, serviceFeeType, memberLevel, overduePostponeDay, deleted, crtTime, uptTime) VALUES ('{0}','0.065', 3, '2', 2, null, null, null, null, null, null, 100, '0', false, '2022-04-18 11:23:03', '2022-04-18 11:23:03');
    """.format(orderNo)

    sql_10 = """INSERT INTO tcbiz_ins_yhc.RepaySchedule (memberId, orderNo, orderType, totalNum, num, repayStatus, repayType, isOverdue, repayDate, payDate, payAmt, overdueNum, initTotalAmt, initPrincipal, initFee, initAdvanceFee, totalAmt, principal, fee, overdue, latestOverdue, latefee, advanceFee, poundage, remainTotalAmt, remainPrincipal, remainFee, remainOverdue, remainLatefee, remainAdvanceFee, waiverFee, waiverAdvanceFee, waiverOverdue, waiverLatefee, waiverPoundage, loanDiscountfee, dayLoanDiscount, payLoanDiscountfee, repayDiscountfee, refundTotalAmt, isFree, discountParty, rotateStatus, deleted, crtTime, uptTime, extAttrs) VALUES ('1251863783', '{0}', 1, 3, 1, 1, 1, false, '2022-05-17', null, 0, 0, 17321, 16346, 975, 0, 16379, 16346, 33, 0, 0, 0, 0, 0, 16379, 16346, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, false, false, 1, false, '2022-04-17 20:49:38', '2022-04-18 00:01:31', null);""".format(
        orderNo)
    sql_11 = """INSERT INTO tcbiz_ins_yhc.RepaySchedule (memberId, orderNo, orderType, totalNum, num, repayStatus, repayType, isOverdue, repayDate, payDate, payAmt, overdueNum, initTotalAmt, initPrincipal, initFee, initAdvanceFee, totalAmt, principal, fee, overdue, latestOverdue, latefee, advanceFee, poundage, remainTotalAmt, remainPrincipal, remainFee, remainOverdue, remainLatefee, remainAdvanceFee, waiverFee, waiverAdvanceFee, waiverOverdue, waiverLatefee, waiverPoundage, loanDiscountfee, dayLoanDiscount, payLoanDiscountfee, repayDiscountfee, refundTotalAmt, isFree, discountParty, rotateStatus, deleted, crtTime, uptTime, extAttrs) VALUES ('1251863783', '{0}', 1, 3, 2, 1, 1, false, '2022-06-17', null, 0, 0, 17321, 16665, 656, 0, 16665, 16665, 0, 0, 0, 0, 0, 0, 16665, 16665, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, false, false, 1, false, '2022-04-17 20:49:38', '2022-04-17 20:49:38', null);""".format(
        orderNo)
    sql_12 = """INSERT INTO tcbiz_ins_yhc.RepaySchedule (memberId, orderNo, orderType, totalNum, num, repayStatus, repayType, isOverdue, repayDate, payDate, payAmt, overdueNum, initTotalAmt, initPrincipal, initFee, initAdvanceFee, totalAmt, principal, fee, overdue, latestOverdue, latefee, advanceFee, poundage, remainTotalAmt, remainPrincipal, remainFee, remainOverdue, remainLatefee, remainAdvanceFee, waiverFee, waiverAdvanceFee, waiverOverdue, waiverLatefee, waiverPoundage, loanDiscountfee, dayLoanDiscount, payLoanDiscountfee, repayDiscountfee, refundTotalAmt, isFree, discountParty, rotateStatus, deleted, crtTime, uptTime, extAttrs) VALUES ('1251863783', '{0}', 1, 3, 3, 1, 1, false, '2022-07-17', null, 0, 0, 17321, 16989, 332, 0, 16989, 16989, 0, 0, 0, 0, 0, 0, 16989, 16989, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, false, false, 1, false, '2022-04-17 20:49:38', '2022-04-17 20:49:38', null);""".format(
        orderNo)
    sql_13 = """INSERT INTO tcbiz_ins_loan.GenFeeLog_202204 ( batchNo, orderNo, num, repayScheduleId, genDate, memberId, genStatus, feeType, operator, calcFee, actualFee, failReason, deleted, crtTime, uptTime, gateId) VALUES ( 'GEN_INT_20220418', '{0}', 1, 20632635, '2022-04-18', '1251863783', 'SUCC', 'INT', 'system', 43, 43, null, false, '2022-04-18 01:33:58', '2022-04-18 01:33:58', 'C001');""".format(
        orderNo)
# print(sql_1)
    cur.execute(sql_1)
    cur.execute(sql_2)
    cur.execute(sql_3)
    cur.execute(sql_4)
    cur.execute(sql_5)
    cur.execute(sql_6)
    cur.execute(sql_7)
    cur.execute(sql_8)
    cur.execute(sql_9)
    cur.execute(sql_10)
    cur.execute(sql_11)
    cur.execute(sql_12)
    cur.execute(sql_13)

    #
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

