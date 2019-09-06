from combos import combo

# Directional Combos
# Down Right (Quarter Circle Right)
QuarterCircleRight = combo("Quarter Circle Right", "Down Right", "Directional")
# Down Left (Quarter Circle Left)
QuarterCircleLeft = combo("Quarter Circle Left", "Down Left", "Directional")
# Left Down Right (Half Circle Right)
HalfCIrcleRight = combo("Half Circle Right", "Left Down Right", "Directional")
# Right Down Left (Half Circle Left)
HalfCircleLeft = combo("Half Circle Left", "Right Down Left", "Directional")
# Left Left (Dash Left)
DashLeft = combo("Dash Left", "Left Left", "Directional")
# Right RIght (Dash Right)
DashRight = combo("Dash Right", "Right Right", "Directional")
# Up Right Right (Air Dash Right)
AirDashRight = combo("Air Dash Right", "Up Right Right", "Directional")
# Up Left Left (Air Dash Left)
AirDashLeft = combo("Air Dash Left", "Up Left Left", "Directional")

# Noncharacter Specifc Auto Combos
LightAutoCombo = combo("Light Auto", "Light Light Light")
MedAutoCombo = combo("Medium Auto", "Medium Medium Medium")
BasicChainCombo = combo("Basic Chain Auto", "Light Medium Heavy")

QuarterCircleRightLight = combo("Quarter Circle Right Light", "Down Right Light")
QuarterCircleLeftLight = combo("Quarter Circle Left Light", "Down Left Light")
QuarterCircleRightMed = combo("Quarter Circle Right Medium", "Down Right Medium")
QuarterCircleLeftMed = combo("Quarter Circle Left Medium", "Down Left Medium")
DownHeavy = combo("Down Heavy (Launcher)", "Down Heavy")
LvlOneSuper = combo("Level One Super", "Down Right Heavy")
LvlThreeSuper = combo("Level Three Super", "Down Left Heavy")

comboDict = {
    DashLeft.comboString : DashLeft,
    DashRight.comboString : DashRight,
    AirDashRight.comboString : AirDashRight,
    AirDashLeft.comboString : AirDashLeft,
    QuarterCircleRightLight.comboString : QuarterCircleRightLight,
    QuarterCircleLeftLight.comboString : QuarterCircleLeftLight,
    QuarterCircleRightMed.comboString : QuarterCircleRightMed,
    QuarterCircleLeftMed.comboString : QuarterCircleLeftMed,
    LightAutoCombo.comboString : LightAutoCombo,
    MedAutoCombo.comboString : MedAutoCombo,
    BasicChainCombo.comboString : BasicChainCombo,
    DownHeavy.comboString : DownHeavy,
    LvlOneSuper.comboString : LvlOneSuper,
    LvlThreeSuper.comboString : LvlThreeSuper
}

