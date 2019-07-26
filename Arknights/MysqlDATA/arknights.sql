/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50725
Source Host           : 192.168.226.129:3306
Source Database       : arknights

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-07-26 17:31:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for akn
-- ----------------------------
DROP TABLE IF EXISTS `akn`;
CREATE TABLE `akn` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `camp` varchar(255) DEFAULT NULL,
  `profession` varchar(255) DEFAULT NULL,
  `gender` int(1) DEFAULT NULL,
  `star` int(11) DEFAULT NULL,
  `characteristic` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `getway` varchar(255) DEFAULT NULL,
  `add_time` datetime DEFAULT NULL,
  `imgsrc` varchar(255) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of akn
-- ----------------------------
INSERT INTO `akn` VALUES ('1', '杜宾', '罗德岛', '近卫', '0', '4', '可以攻击到较远敌人', '近战位、支援、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('2', '推进之王', '维多利亚', '先锋', '0', '6', '能够阻挡两个敌人', '近战位、费用回复、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('3', '白面鸮', '莱茵生命实验室', '医疗', '0', '5', '同时恢复三个友方单位的生命', '远程位、治疗、支援', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('4', '深海色', '罗德岛', '辅助', '0', '4', '攻击造成法术伤害、可以使用召唤物协助作战', '远程位、召唤', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('5', '德克萨斯', '企鹅物流', '先锋', '0', '5', '能够阻挡两个敌人', '控场、近战位、费用回复', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('6', '夜刀', '罗德岛', '先锋', '0', '2', '能够阻挡两个敌人', '近战位、新手', '初始、公开招募', null, null, null);
INSERT INTO `akn` VALUES ('7', '芬', '罗德岛', '先锋', '0', '3', '能够阻挡两个敌人', '近战位、费用回复', '公开招募、干员寻访、教程TR-4首通', null, null, null);
INSERT INTO `akn` VALUES ('8', '芙兰卡', '黑钢国际', '近卫', '0', '5', '能够阻挡一个敌人', '近战位、输出、生存', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('9', '幽灵鲨', '深海猎人', '近卫', '0', '5', '同时攻击阻挡的所有敌人', '近战位、群攻、生存', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('10', '凛冬', '乌萨斯', '先锋', '0', '5', '能够阻挡两个敌人', '支援、近战位、费用回复', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('11', '巡林者', '罗德岛', '狙击', '1', '2', '优先攻击空中单位', '远程位、新手', '初始、公开招募', null, null, null);
INSERT INTO `akn` VALUES ('12', '杜林', '罗德岛', '术师', '0', '2', '攻击造成法术伤害', '远程位、新手', '教程TR-5首通、公开招募', null, null, null);
INSERT INTO `akn` VALUES ('13', '克洛丝', '罗德岛', '狙击', '0', '3', '优先攻击空中单位', '远程位、输出', '公开招募、干员寻访、教程TR-8首通', null, null, null);
INSERT INTO `akn` VALUES ('14', '炎熔', '罗德岛', '术师', '0', '3', '攻击造成群体法术伤害', '远程位、群攻', '公开招募、干员寻访、主线0-8首通', null, null, null);
INSERT INTO `akn` VALUES ('15', '梅', '罗德岛', '狙击', '0', '4', '优先攻击空中单位', '当前暂不实装', '', null, null, null);
INSERT INTO `akn` VALUES ('16', '夜烟', '维多利亚', '术师', '0', '4', '攻击造成法术伤害', '削弱、远程位、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('17', '阿米娅', '罗德岛', '术师', '0', '5', '攻击造成法术伤害', '远程位、输出', '初始、主线2-10、3-8、4-9首通', null, null, null);
INSERT INTO `akn` VALUES ('18', '白雪', '龙门', '狙击', '0', '4', '攻击造成群体物理伤害', '远程位、群攻、减速', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('19', '普罗旺斯', '罗德岛', '狙击', '0', '5', '高精度的近距离射击', '远程位、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('20', '远山', '罗德岛', '术师', '0', '4', '攻击造成群体法术伤害', '远程位、群攻', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('21', '能天使', '企鹅物流', '狙击', '0', '6', '优先攻击空中单位', '远程位、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('22', '蓝毒', '罗德岛', '狙击', '0', '5', '优先攻击空中单位', '远程位、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('23', '流星', '卡西米尔', '狙击', '0', '4', '优先攻击空中单位', '远程位、输出、削弱', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('24', '星熊', '龙门', '重装', '0', '6', '能够阻挡三个敌人', '近战位、输出、防护', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('25', '红', '罗德岛', '特种', '0', '5', '再部署时间大幅减少', '近战位、控场、快速复活', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('26', '黑角', '罗德岛', '重装', '1', '2', '能够阻挡三个敌人', '近战位、新手', '初始、公开招募', null, null, null);
INSERT INTO `akn` VALUES ('27', '末药', '罗德岛', '医疗', '0', '4', '恢复友方单位生命', '远程位、治疗', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('28', '赫默', '莱茵生命实验室', '医疗', '0', '5', '恢复友方单位生命', '远程位、治疗', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('29', '蛇屠箱', '罗德岛', '重装', '0', '4', '能够阻挡三个敌人', '近战位、防护', '公开招募、干员寻访、商店兑换', null, null, null);
INSERT INTO `akn` VALUES ('30', '闪灵', '罗德岛', '医疗', '0', '6', '恢复友方单位生命', '远程位、支援、治疗', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('31', '芙蓉', '罗德岛', '医疗', '0', '3', '恢复友方单位生命', '远程位、治疗', '公开招募、干员寻访、作战演习TR-1首通', null, null, null);
INSERT INTO `akn` VALUES ('32', '米格鲁', '罗德岛', '重装', '0', '3', '能够阻挡三个敌人', '近战位、防护', '公开招募、干员寻访、教程TR-7首通', null, null, null);
INSERT INTO `akn` VALUES ('33', '临光', '罗德岛', '重装', '0', '5', '技能可以治疗友方单位', '近战位、防护、治疗', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('34', '雷蛇', '黑钢国际', '重装', '0', '5', '能够阻挡三个敌人', '近战位、防护、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('35', '伊芙利特', '莱茵生命实验室', '术师', '0', '6', '攻击造成超远距离的群体法术伤害', '远程位、群攻、削弱', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('36', '塞雷娅', '莱茵生命实验室', '重装', '0', '6', '技能可以治疗友方单位', '近战位、支援、防护、治疗', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('37', '银灰', '谢拉格', '近卫', '1', '6', '可以进行远程攻击，但此时攻击力降低至80%', '近战位、输出、支援', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('38', '夜魔', '维多利亚', '术师', '0', '5', '攻击造成法术伤害', '远程位、输出、治疗、减速', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('39', '天火', '罗德岛', '术师', '0', '5', '攻击造成群体法术伤害', '控场、远程位、群攻', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('40', '初雪', '谢拉格', '辅助', '0', '5', '攻击造成法术伤害', '远程位、削弱', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('41', '因陀罗', '维多利亚', '近卫', '0', '5', '能够阻挡一个敌人', '近战位、输出、生存', '公开招募', null, null, null);
INSERT INTO `akn` VALUES ('42', '艾丝黛尔', '罗德岛', '近卫', '0', '4', '同时攻击阻挡的所有敌人', '近战位、群攻、生存', '公开招募', null, null, null);
INSERT INTO `akn` VALUES ('43', '猎蜂', '乌萨斯', '近卫', '0', '4', '能够阻挡一个敌人', '近战位、输出', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('44', '嘉维尔', '罗德岛', '医疗', '0', '4', '恢复友方单位生命', '远程位、治疗', '商店兑换', null, null, null);
INSERT INTO `akn` VALUES ('45', '卡缇', '罗德岛', '重装', '0', '3', '能够阻挡三个敌人', '近战位、防护', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('46', '史都华德', '罗德岛', '术师', '1', '3', '攻击造成法术伤害', '远程位、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('47', '夜莺', '罗德岛', '医疗', '0', '6', '同时恢复三个友方单位的生命', '远程位、治疗、支援', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('48', '艾雅法拉', '卡普里尼', '术师', '0', '6', '攻击造成法术伤害', '远程位、输出、削弱', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('49', '陈', '龙门', '近卫', '0', '6', '普通攻击连续攻击两次', '近战位、爆发', '公开招募、干员寻访', null, null, '2019-07-26 10:35:57');
INSERT INTO `akn` VALUES ('50', '拉普兰德', '罗德岛', '近卫', '0', '5', '可以进行远程攻击，但此时攻击力降低至80%', '近战位、输出、削弱', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('51', '华法琳', '罗德岛', '医疗', '0', '5', '恢复友方单位生命', '远程位、治疗、支援', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('52', '守林人', '罗德岛', '狙击', '0', '5', '优先攻击攻击范围内防御力最低的敌方单位', '远程位、输出、爆发', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('53', '狮蝎', '罗德岛', '特种', '0', '5', '对攻击范围内所有敌人造成伤害、拥有50%的物理和法术闪避且不容易成为敌人的攻击目标', '生存、近战位、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('54', '火神', '罗德岛', '重装', '0', '5', '无法被友方角色治疗', '近战位、输出、防护、生存', '公开招募', null, null, null);
INSERT INTO `akn` VALUES ('55', '真理', '乌萨斯', '辅助', '0', '5', '攻击造成法术伤害，并对敌人造成短暂的停顿', '远程位、减速、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('56', '慕斯', '维多利亚', '近卫', '0', '4', '攻击造成法术伤害', '近战位、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('57', '砾', '卡西米尔', '特种', '0', '4', '再部署时间大幅度减少', '近战位、快速复活、防护', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('58', '暗索', '雷姆必拓', '特种', '0', '4', '技能可以使敌人产生位移、可以放置于远程位', '近战位、位移', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('59', '凯尔希', '罗德岛', '医疗', '0', '6', '恢复友方单位生命、可以使用召唤物协助作战', '当前暂不实装', '', null, null, null);
INSERT INTO `akn` VALUES ('60', '地灵', '卡普里尼', '辅助', '0', '4', '攻击造成法术伤害，并对敌人造成短暂的停顿', '远程位、减速', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('61', '调香师', '罗德岛', '医疗', '0', '4', '同时恢复三个友方单位的生命', '远程位、治疗', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('62', '陨星', '罗德岛', '狙击', '0', '5', '攻击造成群体物理伤害', '远程位、群攻、削弱', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('63', '讯使', '谢拉格', '先锋', '1', '4', '能够阻挡两个敌人', '近战位、费用回复、防护', '商店兑换', null, null, null);
INSERT INTO `akn` VALUES ('64', '白金', '卡西米尔', '狙击', '0', '5', '优先攻击空中单位', '远程位、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('65', '香草', '黑钢国际', '先锋', '0', '3', '能够阻挡两个敌人', '近战位、费用回复', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('66', '梅尔', '莱茵生命实验室', '辅助', '0', '5', '攻击造成法术伤害、可以使用召唤物协助作战', '远程位、召唤、控场', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('67', '可颂', '企鹅物流', '重装', '0', '5', '能够阻挡三个敌人', '近战位、位移、防护', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('68', '崖心', '谢拉格', '特种', '0', '5', '技能可以使敌人产生位移、可以放置于远程位', '输出、近战位、位移', '公开招募、干员寻访、7天签到获得', null, null, null);
INSERT INTO `akn` VALUES ('69', '空', '企鹅物流', '辅助', '0', '5', '不进行攻击，持续恢复攻击范围内所有友军的生命（每秒恢复相当于空攻击力10%的生命）', '支援、远程位、治疗', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('70', '食铁兽', '罗德岛', '特种', '0', '5', '同时攻击阻挡的所有敌人、可以放置于远程位', '减速、近战位、位移', '公开招募、干员寻访、商店兑换', null, null, null);
INSERT INTO `akn` VALUES ('71', '清道夫', '罗德岛', '先锋', '0', '4', '能够阻挡两个敌人', '近战位、费用回复、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('72', '霜叶', '罗德岛', '近卫', '0', '4', '可以进行远程攻击，但此时攻击力降低至80%', '近战位、减速、输出', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('73', '古米', '乌萨斯', '重装', '0', '4', '技能可以治疗友方单位', '近战位、防护、治疗', '公开招募、干员寻访、新手6元礼包', null, null, null);
INSERT INTO `akn` VALUES ('74', '角峰', '谢拉格', '重装', '1', '4', '能够阻挡三个敌人', '近战位、防护', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('75', '断罪者', '罗德岛', '特种', '0', '4', '同时攻击阻挡的所有敌人、技能可以使敌人产生位移', '当前暂不实装', '', null, null, null);
INSERT INTO `akn` VALUES ('76', '玫兰莎', '罗德岛', '近卫', '0', '3', '能够阻挡一个敌人', '近战位、输出、生存', '公开招募、干员寻访、主线0-11首通', null, null, null);
INSERT INTO `akn` VALUES ('77', '安赛尔', '罗德岛', '医疗', '1', '3', '恢复友方单位生命', '远程位、治疗', '公开招募、干员寻访、主线0-10首通', null, null, null);
INSERT INTO `akn` VALUES ('78', '缠丸', '罗德岛', '近卫', '0', '4', '能够阻挡一个敌人', '输出、近战位、生存', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('79', '阿消', '龙门', '特种', '0', '4', '同时攻击阻挡的所有敌人、可以放置于远程位', '近战位、位移', '公开招募、干员寻访、主线1-12首通', null, null, null);
INSERT INTO `akn` VALUES ('80', '安洁莉娜', '罗德岛', '辅助', '0', '6', '攻击造成法术伤害，并对敌人造成短暂的停顿', '远程位、减速、输出、支援', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('81', '红豆', '罗德岛', '先锋', '0', '4', '击杀敌人后获得1点部署费用，撤退时返还初始部署费用', '近战位、输出、费用回复', '公开招募、干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('82', '暴行', '雷姆必拓', '近卫', '0', '5', '同时攻击阻挡的所有敌人', '近战位、群攻、爆发', '公测累计预约80万人次预约限定奖励', null, null, null);
INSERT INTO `akn` VALUES ('83', '杰西卡', '黑钢国际', '狙击', '0', '4', '优先攻击空中单位', '远程位、输出、生存', '公开招募、干员寻访、教程TR-3首通', null, null, null);
INSERT INTO `akn` VALUES ('84', '12F', '罗德岛', '术师', '1', '2', '攻击造成群体法术伤害', '远程位、新手', '教程TR-6首通、公开招募', null, null, null);
INSERT INTO `akn` VALUES ('85', '梓兰', '罗德岛', '辅助', '0', '3', '攻击造成法术伤害，并对敌人造成短暂的停顿', '远程位、减速', '公开招募、干员寻访、主线1-7首通', null, null, null);
INSERT INTO `akn` VALUES ('86', '翎羽', '拉特兰', '先锋', '0', '3', '击杀敌人后获得1点部署费用，撤退时返还初始部署费用', '近战位、输出、费用回复', '公开招募、干员寻访、主线0-5首通', null, null, null);
INSERT INTO `akn` VALUES ('87', 'Lancet-2', '罗德岛', '医疗', '0', '1', '恢复友方单位生命，且不受部署数量限制，但再部署时间极长', '远程位、治疗', '教程TR-10首通、公开招募', null, null, null);
INSERT INTO `akn` VALUES ('88', 'Castle-3', '罗德岛', '近卫', '1', '1', '能够阻挡一个敌人，且不受部署数量限制，但再部署时间极长', '近战位、支援', '公开招募', null, null, null);
INSERT INTO `akn` VALUES ('89', '安德切尔', '罗德岛', '狙击', '1', '3', '优先攻击空中单位', '远程位、输出', '教程TR-2首通、公开招募', null, null, null);
INSERT INTO `akn` VALUES ('90', '空爆', '罗德岛', '狙击', '0', '3', '攻击造成群体物理伤害', '远程位、群攻', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('91', '斯卡蒂', '深海猎人', '近卫', '0', '6', '能够阻挡一个敌人', '近战位、输出、生存', '干员寻访', null, null, null);
INSERT INTO `akn` VALUES ('92', '格拉尼', '维多利亚', '先锋', '0', '5', '击杀敌人后获得1点部署费用，撤退时返还部署费用', '近战位、费用回复、防护', '「骑兵与猎人」活动GT-3首通限定', null, null, null);
INSERT INTO `akn` VALUES ('93', '月见夜', '罗德岛', '近卫', '1', '3', '可以进行远程攻击，但此时攻击力降低至80%', '近战位、输出', '干员寻访', null, null, '2019-07-22 11:46:50');

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('91d5cf89d399');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `add_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `ix_user_email` (`email`),
  KEY `ix_user_status` (`status`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', 'ff9830c42660c1dd1942844f8069b74a', 'admin@akn.com', '1', '1', null, '2019-07-19 06:41:53', '2019-07-23 10:24:37');
INSERT INTO `user` VALUES ('3', 'test', 'dc483e80a7a0bd9ef71d8cf973673924', 'a@b.com', '0', '1', null, '2019-07-23 08:27:43', '2019-07-23 08:27:43');
