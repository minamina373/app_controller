# �v���W�F�N�g��

Python�Ńv���O���������Ԃɒ���I�Ɏ��s����X�N���v�g


---

## �ڎ�

- [�T�v](#�T�v)
- [�@�\](#�@�\)
- [����](#����)


---

## �T�v

app_controller.py�@�t�@�C�������s���邱�Ƃɂ��z���̃v���O�����𓮓I�ɓǂݍ��ݎ��s��������A�y�ʂ̃T�[�r�X�R���g���[���ł��F

- ����/�t���[�����[�N:  Python


---

## �@�\

- app_controller.py�@�͑S�ẴT�[�r�X���R���g���[������t�@�C���ł�
- app_base.py ���p�������z���̃v���O�������쐬���܂��A���̃t�@�C�������I�ɃC���|�[�g����t�@�C����u�������ŏ���Ɏ��s����܂�

- �t�@�C�����K����
- ���_���O_�o�[�W����(�����A�����A�傫���ق����ŐV�A�o�[�W�����͖����ł��s���܂�)
- ��ނ́@setting ,process, module 
- ���s����setting ��process�� module ��setting 
-  setting:�@���[�v�̍ŏ���on_setting_load �����s����܂��@public_values�ɓ��ꂽ�l��setting_value�Ƃ���process,module�Ɉ����p����܂��A���ʐݒ�擾�⃍�O�̊J�n�Ɏg���܂��ʏ��1�������܂���
-  process: setting�̎��Ɏ��s����܂��A���C���̃f�[�^�擾�����ł��Apublic_value�ɓ��ꂽ�l��module�Ɉ����p����܂�
-  module: process�̎��Ɏ��s����܂��Aprocess�ō쐬�����l�����Ƃɏ������s���܂�
-  setting: ���[�v�̍Ō��on_setting_end�𔭉΂����邽�ߎ��s����܂�
- �C�x���g��			
- on_setting_load (event_state��1�̏ꍇ�̂ݎ��s����܂�
- on_load
- on_process_event�imodule�̏ꍇ��process����󂯎����public_values�̐��������s���܂��j
- on_end
- on_setting_end (event_state��2�̏ꍇ�̂ݎ��s����܂�
- �̏��ԂŃC�x���g�Ƃ����s����܂�
- on_setting load end ��setting���W���[���ł������΂��܂���
- �z���̃N���X�́@app_base.py�@���p�����ꂽ�N���X�������삵�܂���A�Ȃ̂Őe�N���X�p�̂��̃t�@�C�����K�v�ł�


---

## ����

- �I�I�z���̃N���X���͓��삵���������ΕύX����ȁI�I
- �o�[�W�������オ�邱�Ƃɂ���ăt�@�C�����̃N���X���������ł���Βl�����L�ł��܂�
- �o�[�W�������グ�ăN���X����ύX����ƒl�����L�ł��܂��񂵁A�����N���邩�킩��܂���A�N���X���͐�ΕҏW���Ă͂����܂���

