# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-
from cereal import car, log

# Priority
class Priority:
  LOWEST = 0
  LOW_LOWEST = 1
  LOW = 2
  MID = 3
  HIGH = 4
  HIGHEST = 5

AlertSize = log.ControlsState.AlertSize
AlertStatus = log.ControlsState.AlertStatus
AudibleAlert = car.CarControl.HUDControl.AudibleAlert
VisualAlert = car.CarControl.HUDControl.VisualAlert

class Alert(object):
  def __init__(self,
               alert_type,
               alert_text_1,
               alert_text_2,
               alert_status,
               alert_size,
               alert_priority,
               visual_alert,
               audible_alert,
               duration_sound,
               duration_hud_alert,
               duration_text,
               alert_rate=0.):

    self.alert_type = alert_type
    self.alert_text_1 = alert_text_1
    self.alert_text_2 = alert_text_2
    self.alert_status = alert_status
    self.alert_size = alert_size
    self.alert_priority = alert_priority
    self.visual_alert = visual_alert
    self.audible_alert = audible_alert

    self.duration_sound = duration_sound
    self.duration_hud_alert = duration_hud_alert
    self.duration_text = duration_text

    self.start_time = 0.
    self.alert_rate = alert_rate

    # typecheck that enums are valid on startup
    tst = car.CarControl.new_message()
    tst.hudControl.visualAlert = self.visual_alert

  def __str__(self):
    return self.alert_text_1 + "/" + self.alert_text_2 + " " + str(self.alert_priority) + "  " + str(
      self.visual_alert) + " " + str(self.audible_alert)

  def __gt__(self, alert2):
    return self.alert_priority > alert2.alert_priority


ALERTS = [
  # Miscellaneous alerts
  Alert(
      "enable",
      "",
      "",
      AlertStatus.normal, AlertSize.none,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeEngage, .2, 0., 0.),

  Alert(
      "disable",
      "",
      "",
      AlertStatus.normal, AlertSize.none,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeDisengage, .2, 0., 0.),

  Alert(
      "fcw",
      "剎車!",
      "有碰撞的風險",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.fcw, AudibleAlert.chimeWarningRepeat, 1., 2., 2.),

  Alert(
      "steerSaturated",
      "接管控制",
      "彎道超過方向盤轉向限制",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimePrompt, 1., 2., 3.),

  Alert(
      "steerTempUnavailable",
      "接管控制",
      "轉向控制暫時失效",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimeWarning1, .4, 2., 3.),

  Alert(
      "steerTempUnavailableMute",
      "接管控制",
      "轉向控制暫時失效",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .2, .2, .2),

  Alert(
      "preDriverDistracted",
      "注意路況: 駕駛出現分心",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "promptDriverDistracted",
      "注意路況",
      "駕駛出現分心",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, .1, .1),

  Alert(
      "driverDistracted",
      "立即解除",
      "駕駛出現分心",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "preDriverUnresponsive",
      "觸碰方向盤: 無駕駛監控",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "promptDriverUnresponsive",
      "觸碰方向盤",
      "駕駛沒有反應",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, .1, .1),

  Alert(
      "driverUnresponsive",
      "立即解除",
      "駕駛沒有反應",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "driverMonitorOff",
      "駕駛監控暫時停用",
      "監控準確率: 低",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .4, 0., 4.),

  Alert(
      "driverMonitorOn",
      "駕駛監控已啟用",
      "監控準確率: 高",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .4, 0., 4.),

  Alert(
      "geofence",
      "DISENGAGEMENT REQUIRED",
      "不在地理圍欄區域之內",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "startup",
      "隨時準備好接管",
      "請您將手放在方向盤上並持續注意路況",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "startupNoControl",
      "行車記錄器模式",
      "請您將手放在方向盤上並持續注意路況",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "startupNoCar",
      "行車記錄器模式 (未支持的車型)",
      "請您將手放在方向盤上並持續注意路況",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "ethicalDilemma",
      "即刻接管控制",
      "Ethical Dilemma Detected",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 3.),

  Alert(
      "steerTempUnavailableNoEntry",
      "無法使用 openpilot",
      "轉向控制暫時失效",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "manualRestart",
      "接管控制",
      "請自行恢復駕駛",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "resumeRequired",
      "已停止",
      "請按 RES 繼續",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "belowSteerSpeed",
      "接管控制",
      "轉向控制暫時失效，車速低於 ",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning1, 0., 0., .1),

  Alert(
      "debugAlert",
      "DEBUG ALERT",
      "",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .1, .1, .1),

  # Non-entry only alerts
  Alert(
      "wrongCarModeNoEntry",
      "無法使用 openpilot",
      "主開關關閉",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "dataNeededNoEntry",
      "無法使用 openpilot",
      "需要更多的數據來協助校準，請將行車記錄上傳後再試",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "outOfSpaceNoEntry",
      "無法使用 openpilot",
      "儲存空間不足",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "pedalPressedNoEntry",
      "無法使用 openpilot",
      "Pedal Pressed During Attempt",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, "brakePressed", AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "speedTooLowNoEntry",
      "無法使用 openpilot",
      "車速過慢",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "brakeHoldNoEntry",
      "無法使用 openpilot",
      "駐車煞車已啟用",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "parkBrakeNoEntry",
      "無法使用 openpilot",
      "電子駐車已啟動",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "lowSpeedLockoutNoEntry",
      "無法使用 openpilot",
      "巡航系統錯誤: 請重新發動車輛",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "lowBatteryNoEntry",
      "無法使用 openpilot",
      "電池電量過低",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "sensorDataInvalidNoEntry",
      "無法使用 openpilot",
      "沒有收到任何來自 EON 傳感器的數據",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  # Cancellation alerts causing soft disabling
  Alert(
      "overheat",
      "即刻接管控制",
      "系統過熱",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "wrongGear",
      "即刻接管控制",
      "檔位不在 D 檔",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "calibrationInvalid",
      "即刻接管控制",
      "校準無效: 請將 EON 放於新的位置並重新校準",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "calibrationIncomplete",
      "即刻接管控制",
      "正在校準相機中",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "doorOpen",
      "即刻接管控制",
      "車門開啟",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "seatbeltNotLatched",
      "即刻接管控制",
      "安全帶未繫",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "espDisabled",
      "即刻接管控制",
      "ESP 關閉",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "lowBattery",
      "即刻接管控制",
      "電池電量過低",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  # Cancellation alerts causing immediate disabling
  Alert(
      "radarCommIssue",
      "即刻接管控制",
      "雷達訊號錯誤: 請重新發動車輛",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "radarFault",
      "即刻接管控制",
      "雷達訊號錯誤: 請重新發動車輛",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "modelCommIssue",
      "即刻接管控制",
      "AI 模型錯誤: 請檢查網路連線",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "controlsFailed",
      "即刻接管控制",
      "控制發生錯誤",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "controlsMismatch",
      "即刻接管控制",
      "控制不匹配",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "commIssue",
      "即刻接管控制",
      "CAN 訊號錯誤: 請檢查接線",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "steerUnavailable",
      "即刻接管控制",
      "LKAS 錯誤: 請重新發動車輛",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "brakeUnavailable",
      "即刻接管控制",
      "巡航系統錯誤: 請重新發動車輛",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "gasUnavailable",
      "即刻接管控制",
      "油門錯誤: 請重新發動車輛",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "reverseGear",
      "即刻接管控制",
      "切換至倒車檔",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "cruiseDisabled",
      "即刻接管控制",
      "巡航系統關閉",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "plannerError",
      "即刻接管控制",
      "Planner Solution 出現錯誤",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  # not loud cancellations (user is in control)
  Alert(
      "noTarget",
      "openpilot 已取消",
      "沒有偵測到前車",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "speedTooLow",
      "openpilot 已取消",
      "車速過慢",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "invalidGiraffeHonda",
      "Giraffe 開關錯誤",
      "openpilot 模式為 0111，原廠模式為 1011",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  # Cancellation alerts causing non-entry
  Alert(
      "overheatNoEntry",
      "無法使用 openpilot",
      "系統過熱",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "wrongGearNoEntry",
      "無法使用 openpilot",
      "車輛不在 D 檔",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "calibrationInvalidNoEntry",
      "無法使用 openpilot",
      "校準無效: 請將 EON 放於新的位置並重新校準",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "calibrationIncompleteNoEntry",
      "無法使用 openpilot",
      "正在校準相機中",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "doorOpenNoEntry",
      "無法使用 openpilot",
      "車門未關",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "seatbeltNotLatchedNoEntry",
      "無法使用 openpilot",
      "安全帶未繫",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "espDisabledNoEntry",
      "無法使用 openpilot",
      "ESP 關閉",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "geofenceNoEntry",
      "無法使用 openpilot",
      "不在地理圍欄區域之內",
      AlertStatus.normal, AlertSize.mid,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "radarCommIssueNoEntry",
      "無法使用 openpilot",
      "雷達訊號錯誤: 請重新發動車輛",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "radarFaultNoEntry",
      "無法使用 openpilot",
      "雷達訊號錯誤: 請重新發動車輛",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "modelCommIssueNoEntry",
      "無法使用 openpilot",
      "AI 模型錯誤: 請檢查網路連線",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "controlsFailedNoEntry",
      "無法使用 openpilot",
      "控制發生錯誤",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "commIssueNoEntry",
      "無法使用 openpilot",
      "CAN 訊號錯誤: 請檢查接線",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "steerUnavailableNoEntry",
      "無法使用 openpilot",
      "LKAS 錯誤: 請重新發動車輛",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "brakeUnavailableNoEntry",
      "無法使用 openpilot",
      "巡航系統錯誤: 請重新發動車輛",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "gasUnavailableNoEntry",
      "無法使用 openpilot",
      "油門錯誤: 請重新發動車輛",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "reverseGearNoEntry",
      "無法使用 openpilot",
      "切換至倒車檔",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "cruiseDisabledNoEntry",
      "無法使用 openpilot",
      "巡航系統關閉",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "noTargetNoEntry",
      "無法使用 openpilot",
      "沒有偵測到前車",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "plannerErrorNoEntry",
      "無法使用 openpilot",
      "Planner Solution 出現錯誤",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "invalidGiraffeHondaNoEntry",
      "無法使用 openpilot",
      "penpilot 模式為 0111，原廠模式為 1011",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  # permanent alerts
  Alert(
      "steerUnavailablePermanent",
      "LKAS 錯誤: 請重新發動車輛",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "brakeUnavailablePermanent",
      "巡航系統錯誤: 請重新發動車輛",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "lowSpeedLockoutPermanent",
      "巡航系統錯誤: 請重新發動車輛",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "calibrationIncompletePermanent",
      "正在校準相機中: ",
      "車速請高於 ",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "invalidGiraffeHondaPermanent",
      "Giraffe 開關錯誤",
      "penpilot 模式為 0111，原廠模式為 1011",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "sensorDataInvalidPermanent",
      "沒有收到任何來自 EON 傳感器的數據",
      "請重啟您的 EON",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "vehicleModelInvalid",
      "車輛參數識別失敗",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOWEST, VisualAlert.steerRequired, AudibleAlert.none, .0, .0, .1),
]
